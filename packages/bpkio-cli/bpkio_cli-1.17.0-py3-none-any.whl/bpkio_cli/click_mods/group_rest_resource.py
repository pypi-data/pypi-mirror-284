import re
from typing import Any

import bpkio_api.models as models
import click
import cloup

from bpkio_cli.core.resource_trail import ResourceTrail
from bpkio_cli.writers.breadcrumbs import display_context


class ApiResourceGroup(cloup.Group):
    """A click.Group sub-class that enables the use of command lines that
    1.  mirror REST endpoint structure that use resource identifiers
        (eg. `mycli sources 123 slots 456`
        -> http://myapi/sources/:source_id/slots/:slot_id)
    2.  allow for implicit commands for `list` and `get` when no sub-commands are
        provided on parent groups that support it.
        (eg. `mycli sources` -> `mycli sources list`)
        (eg. `mycli sources 123` -> `mycli sources 123 get`)
    3.  save automatically the ID to the context (for use deeper in the chain)

    Inspired by https://stackoverflow.com/a/44056564/2215413"""

    def __init__(self, *args: Any, resource_class: type | None = None, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.resource_class = resource_class

    def parse_args(self, ctx, args):
        commands_without_resource_id = ["list", "search", "create", "select", "set"]

        # No sub-command?  Then it's an implicit `list`
        #  eg. "bic sources" -> "bic sources list"
        if len(args) == 0 and "list" in self.commands:
            args.append("list")
            display_context(
                "No sub-command provided, assuming 'list'.",
            )

        # Some commands do not take an ID argument,
        # so inject an empty one to prevent parse failure
        #  eg. "bic sources list" -> "bic sources '' list"
        if args[0] in commands_without_resource_id:
            args.insert(0, "")

        # If the first argument is a command that normally takes an ID,
        # but there is a "--help", inject an empty one to allow normal behaviour
        #  eg. "bic sources get --help" -> "bic sources '' get --help"
        if args[0] in self.commands and any(a in args for a in ["--help"]):
            args.insert(0, "")

        # If the first argument is "--id" (which is only used to make it easier to do auto-complete), we simply remove it
        if args[0] in ["--id", "-i"]:
            args.pop(0)

        # Single argument, which is not a command?
        # It must be an ID, and we treat it as an implicit `get`
        #  eg. "bic sources 123" -> "bic sources 123 get"
        #  eg. "bic sources 123 --help" -> "bic sources 123 get --help"
        if args[0] not in self.commands and args[0] not in self.alias2name:
            if (len(args) == 1) or (len(args) == 2 and args[1] in ["--help"]):
                args.insert(1, "get")
                display_context(
                    "No sub-command provided, assuming 'get'.",
                )

        # If the command is one that require an ID, but there isn't one, it's an error
        #  eg. "bic sources get" -> BadArgumentUsage
        if (args[0] in self.commands or args[0] in self.alias2name) and (
            args[0] not in commands_without_resource_id
        ):
            display_context(
                "No ID provided, using '$' to reuse the previous resource.",
            )
            args.insert(0, "$")
            # raise click.BadArgumentUsage(
            #     f"The `{args[0]}` command must be preceded by a {self.name} ID"
            # )

        # If there is a resource-based command preceded by a non-empty string,
        # that's an error
        #  eg. "bic sources 123 list" -> BadArgumentUsage
        if args[0] != "" and args[1] in [
            c for c in commands_without_resource_id if c != "json"
        ]:
            raise click.BadArgumentUsage(
                f"The `{args[1]}` command cannot be preceded by a resource ID"
            )

        # actual (non-empty) argument before command?  It's an ID,
        # and we save it automatically to the context object
        #  eg. "bic sources 123 get" -> record ID '123'
        if (
            args[0] != ""
            and args[0] not in self.commands
            and (args[1] in self.commands or args[1] in self.alias2name)
        ):
            target_type = self._get_resource_class_for_command()

            # Lookup in the cache if the ID is not a recognised value
            if (
                not args[0].isdigit()
                and not args[0].startswith("-")
                and not args[0].startswith("http")
            ):
                placeholder = args[0]
                args[0] = ctx.obj.cache.resolve(placeholder, target_type)
                if placeholder != args[0]:
                    display_context(
                        f"Resolved '{placeholder}' to {target_type.__name__} with id '{args[0]}'",
                    )

            resources: ResourceTrail = ctx.obj.resources
            resources.record_resource_id(self.name, args[0])

        super(ApiResourceGroup, self).parse_args(ctx, args)

    def full_command_name(self, ctx):
        """Generate an optionally composite command name
        by traversing the chain of commands to the current one
        """
        cmd = ctx.command.name
        if hasattr(ctx, "parent"):
            if ctx.parent.command.name != "bic":
                cmd = self.full_command_name(ctx.parent) + ":" + cmd
        return cmd

    def _get_resource_class_for_command(self):
        if self.resource_class:
            return self.resource_class
        else:
            return models.BaseResource
