import json as j
from typing import List, Optional

import bpkio_cli.click_options as bic_options
import click
import cloup
from bpkio_api.helpers.handlers import ContentHandler, factory
from bpkio_api.helpers.handlers.dash import DASHHandler
from bpkio_api.helpers.handlers.hls import HLSHandler
from bpkio_api.helpers.source_type import SourceTypeDetector
from bpkio_api.models import SourceType
from bpkio_cli.click_mods import ApiResourceGroup
from bpkio_cli.commands.sources import create as source_create
from bpkio_cli.commands.misc.compatibility_check import check_compatibility
from bpkio_cli.core.app_context import AppContext
from bpkio_cli.core.config_provider import CONFIG
from bpkio_cli.core.exceptions import BroadpeakIoCliError
from bpkio_cli.monitor.live_monitor import monitor_hls
from bpkio_cli.utils.profile_maker import make_transcoding_profile
from bpkio_cli.utils.url_builders import ask_for_user_agent
from bpkio_cli.writers.colorizer import Colorizer as CL
from bpkio_cli.writers.content_display import display_content
from bpkio_cli.writers.players import StreamPlayer
from bpkio_cli.writers.tables import display_table
from pydantic import HttpUrl, parse_obj_as


def determine_source_type(full_url) -> SourceType | None:
    source_type = SourceTypeDetector.determine_source_type(full_url)
    if not source_type:
        click.secho(
            "Could not determine the type of source for that URL", fg="red", bold="true"
        )
        return None
    else:
        return source_type


def get_handler(
    sub: int | None = None, user_agent: str | None = None, headers: List[str] = []
) -> ContentHandler:
    ctx = click.get_current_context()
    url = ctx.obj.resources.last()

    if user_agent == "SELECT":
        ask_for_user_agent(url)

    handler: ContentHandler = factory.create_handler(
        url,
        user_agent=CONFIG.get_user_agent(user_agent),
        explicit_headers=headers,
    )

    if not sub:
        return handler
    else:
        if handler.has_children():
            return handler.get_child(sub)
        else:
            if not isinstance(handler, DASHHandler):
                click.secho(
                    "`--sub` cannot be used with this source, as it has no children URLs. Using main URL instead",
                    fg="red",
                )
            return handler


# Group: URLs
@cloup.group(
    cls=ApiResourceGroup, help="Work directly with URLs", resource_class=HttpUrl
)
@cloup.argument(
    "full_url",
    help=("The URL to work with"),
)
@click.pass_obj
def url(obj: AppContext, full_url: HttpUrl):
    full_url = parse_obj_as(HttpUrl, full_url)
    obj.current_resource = full_url
    obj.cache.record(full_url)


# --- INFO Commmand
@cloup.command(
    aliases=["content"],
    help="Get detailed information about the content of a URL",
)
@bic_options.url
def info(
    url: str, fqdn: str, query: List[str], header: List[str], user_agent: str, **kwargs
):
    handler = get_handler(None, user_agent, header)

    if handler:
        try:
            display_content(
                handler=handler,
                max=1,
                interval=0,
                table=True,
                trim=0,
            )
        except BroadpeakIoCliError as e:
            pass


# Command: CHECK
@cloup.command(help="Checks the type and validity of a URL")
@bic_options.list()
@bic_options.output_formats
@click.pass_obj
def check(
    obj: AppContext, select_fields, sort_fields, list_format, return_first, **kwargs
):
    full_url = obj.resources.last()
    source_type = determine_source_type(full_url)

    click.secho("This appears to be a source of type: %s" % source_type.value)

    if source_type:
        results = obj.api.sources.check(type=source_type, url=full_url)

        obj.response_handler.treat_list_resources(
            results,
            format=list_format,
            select_fields=select_fields,
            sort_fields=sort_fields,
            return_first=return_first,
        )


# --- READ Command
@cloup.command(
    help="Loads and displays the content of a URL"
    ", optionally highlighted with relevant information"
)
@bic_options.read
@bic_options.url
@bic_options.table
def read(
    sub: int,
    table: bool,
    raw: bool,
    top: bool,
    tail: bool,
    pager: bool,
    ad_pattern: str,
    user_agent: str,
    header: List[str],
    trim: int,
    **kwargs,
):
    handler = get_handler(sub, user_agent, header)

    display_content(
        handler=handler,
        max=1,
        interval=0,
        table=table,
        raw=raw,
        top=top,
        tail=tail,
        pager=pager,
        trim=trim,
        ad_pattern=ad_pattern,
    )


# --- POLL Command
@cloup.command(help="Similar to `read`, but regularly re-load the URL's content")
@bic_options.read
@bic_options.url
@bic_options.poll
@bic_options.table
def poll(
    sub: int,
    user_agent: str,
    header: List[str],
    max: int,
    interval: Optional[int],
    raw: bool,
    diff: bool,
    top: bool,
    tail: bool,
    pager: bool,
    clear: bool,
    table: bool,
    silent: bool,
    trim: int,
    ad_pattern: str,
    **kwargs,
):
    if not sub:
        sub = 1

    handler = get_handler(sub, user_agent, header)

    display_content(
        handler=handler,
        max=max,
        interval=interval,
        table=table,
        raw=raw,
        diff=diff,
        top=top,
        tail=tail,
        pager=pager,
        clear=clear,
        silent=silent,
        trim=trim,
        ad_pattern=ad_pattern,
    )


# --- MONITOR Command
@cloup.command(help="Check a live stream for significant markers")
@bic_options.url
@bic_options.read
@bic_options.poll
@bic_options.monitor
@click.option(
    "--silent",
    help="Turn off audible alerts",
    is_flag=True,
    default=False,
)
def monitor(
    user_agent: str,
    sub: int,
    max: int,
    interval: Optional[int],
    silent: bool,
    header: str,
    with_schedule: bool,
    with_map: bool,
    with_signals: bool,
    with_adinfo: bool,
    with_frames: bool,
    ad_pattern: str,
    **kwargs,
):
    handler = get_handler(sub, user_agent, header)

    source_type = determine_source_type(handler.url)

    if source_type != SourceType.LIVE:
        raise BroadpeakIoCliError(
            "Monitoring can only be done for Live resources (sources or services)"
        )

    if isinstance(handler, DASHHandler):
        raise NotImplementedError(
            "Monitoring of DASH streams not yet implemented in BIC"
        )

    if isinstance(handler, HLSHandler) and handler.has_children():
        handler = handler.get_child(1)
        monitor_hls(
            handler,
            max,
            interval,
            silent,
            with_schedule=with_schedule,
            with_map=with_map,
            with_signals=with_signals,
            with_adinfo=with_adinfo,
            with_frames=with_frames,
            ad_pattern=ad_pattern,
        )


# --- PLAY Command
@cloup.command(help="Open the URL in a web player", aliases=["open"])
@click.option(
    "-s",
    "--sub",
    type=int,
    default=None,
    help="For HLS, reads a sub-playlist (by index - "
    "as given by the `read ID --table` option with the main playlist)",
)
@click.option(
    "-p",
    "--player",
    default="CONFIG",
    help="The template for a player URL",
    type=str,
    is_flag=False,
    flag_value="CHOICE",
)
def play(sub: int, player: str):
    handler = get_handler(sub)

    if player == "CONFIG":
        player = CONFIG.get("default-player")

    if player == "CHOICE":
        player = StreamPlayer.prompt_player()

    StreamPlayer().launch(stream_url=handler.url, key=player, name="")


# --- CREATE Command
@cloup.command(help="Create a Source from the URL")
@cloup.option("--name", help="Name for the source", required=False)
@click.pass_context
def store(ctx, name):
    full_url = ctx.obj.resources.last()

    ctx.invoke(source_create, url=full_url, name=name)


# --- PROFILE Command
@cloup.command(help="Create a Transcoding Profile from the content of the URL")
@bic_options.url
@click.option(
    "--table/--no-table",
    "with_table",
    is_flag=True,
    default=False,
    help="Add or hide summary information about the content of the resource",
)
@click.option(
    "--schema",
    type=str,
    default="bkt-v2",
    help="Version of the transcoding profile schema",
)
@click.option(
    "--name",
    type=str,
    default="",
    help="Name for the transcoding profile",
)
@click.option(
    "--save",
    is_flag=True,
    default=False,
    help="Save the profile to a file",
)
@click.pass_obj
def profile(
    obj: AppContext,
    with_table: bool,
    save: bool,
    schema: int,
    name: str,
    sub: str,
    header: str,
    user_agent: str,
    **kwargs,
):
    handler = get_handler(sub, user_agent, header)

    (profile, messages) = make_transcoding_profile(
        handler, schema_version=schema, name=name
    )

    if with_table:
        display_table(profile["transcoding"]["jobs"])
    else:
        obj.response_handler.treat_single_resource(profile, format="json")

    if save:
        filename = "profile.json"
        with open(filename, "w") as f:
            j.dump(profile, f, indent=4)
        click.secho(f"Profile saved to {filename}", fg="green")

    if messages:
        for message in messages:
            click.echo(CL.log(message.message, message.level), err=True)
        click.secho(
            "Since errors or warnings have been raised, you may want to review the profile payload to ensure it is usable",
            fg="yellow",
            err=True,
        )


url.add_section(
    cloup.Section("Content Commands", [check, info, read, poll, monitor, play, profile])
)

url.add_section(cloup.Section("Other Commands", [store, check_compatibility]))
