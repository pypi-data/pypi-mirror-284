from bpkio_api.helpers.handlers.generic import ContentHandler
from bpkio_cli.writers.colorizer import Colorizer
import click
from bpkio_api import DEFAULT_FQDN

from bpkio_cli.core.config_provider import CONFIG


def display_warning(text):
    click.secho("❕ " + Colorizer.warning(text), err=True)


def display_error(text):
    click.secho("‼️ " + Colorizer.error(text), err=True)


def display_resource_info(resource):
    if CONFIG.get("verbose", int) > 0:
        core_info = "{} {}".format(resource.__class__.__name__, resource.id)
        name = resource.name if hasattr(resource, "name") else ""

        info = "[{c}]  {n}".format(c=core_info, n=name)

        click.secho(info, err=True, fg="white", bg="blue", dim=False)


def display_tenant_info(tenant):
    if CONFIG.get("verbose", int) > 0:
        info = "[Tenant {i}] - {n}".format(i=tenant.id, n=tenant.name)
        if url := tenant._fqdn:
            if url != DEFAULT_FQDN:
                info = info + f" - ({url})"

        click.secho(info, err=True, fg="green", bg="blue", dim=False)


def display_context(message):
    if CONFIG.get("verbose", int) > 1:
        click.secho(
            "💡 " + message,
            fg="magenta",
            # dim=True,
            err=True,
            italic=True,
        )


def display_bpkio_session_info(handler: ContentHandler):
    if hasattr(handler, "session_id") and handler.session_id is not None:
        click.secho(
            Colorizer.labeled(handler.service_id, "service")
            + "  "
            + Colorizer.labeled(handler.session_id, "session"),
            err=True,
        )
