"""app rule command for engineai CLI."""

from typing import Optional

import click
from rich.console import Console
from rich.table import Table

from engineai.sdk.cli.utils import write_console
from engineai.sdk.dashboard.clients.mutation.app_api import AppAPI
from engineai.sdk.internal.clients.exceptions import APIServerError
from engineai.sdk.internal.exceptions import UnauthenticatedError

APP_AUTHORIZATION_ROLE = ["ADMIN", "WRITER", "READER"]


@click.group()
def rule():
    """App rule commands."""


@rule.command(
    "add",
    help="""Add an authorization rule for the user in the app.

        \b
        ACCOUNT_NAME: account to be updated.
        APP_NAME: app to be updated.
        ROLE: role for the user/user group in the app (ADMIN, WRITER OR READER).
        """,
)
@click.argument(
    "account_name",
    required=True,
    type=str,
)
@click.argument(
    "app_name",
    required=True,
    type=str,
)
@click.option(
    "-u",
    "--user",
    required=False,
    type=str,
    help="the user to apply new rules.",
)
@click.option(
    "-ug",
    "--user-group",
    required=False,
    type=str,
    help="the user group to apply new rules.",
)
@click.argument(
    "role",
    required=True,
    type=click.Choice(APP_AUTHORIZATION_ROLE, case_sensitive=False),
)
def add_app_authorization_rule(
    account_name: str,
    app_name: str,
    user: Optional[str],
    user_group: Optional[str],
    role: str,
) -> None:
    """Add an authorization rule for the user/user group in the app.

    Args:
        account_name: account to be updated.
        app_name: app to be updated.
        user: the user to apply new rules.
        user_group: the user group to apply new rules.
        role: role for the user/user group in the app (ADMIN, WRITER OR READER).
    """
    if user is None and user_group is None:
        write_console("Please provide either user or user group\n", 1)
        return

    authorization_role = role.upper()
    api = AppAPI()
    try:
        api.add_app_authorization_rule(
            account_name,
            app_name,
            user,
            user_group,
            authorization_role,
        )
        subject = f"user `{user}`" if user is not None else f"user group `{user_group}`"
        write_console(
            f"Successfully added new authorization rule for {subject} in app "
            f"`{app_name}` within account `{account_name}` with role "
            f"`{authorization_role}`\n",
            0,
        )
    except (APIServerError, UnauthenticatedError) as e:
        write_console(f"{e}\n", 1)


@rule.command(
    "update",
    help="""Update app authorization rule to the user/user group in the app.

                \b
                ACCOUNT_NAME: account to be updated.
                APP_NAME: app to be updated.
                ROLE: role for the user/user group in the app (ADMIN, WRITER OR READER).
    """,
)
@click.argument(
    "account_name",
    required=True,
    type=str,
)
@click.argument(
    "app_name",
    required=True,
    type=str,
)
@click.option(
    "-u",
    "--user",
    required=False,
    type=str,
    help="the user to apply new rules.",
)
@click.option(
    "-ug",
    "--user-group",
    required=False,
    type=str,
    help="the user group to apply new rules.",
)
@click.argument(
    "role",
    required=True,
    type=click.Choice(APP_AUTHORIZATION_ROLE, case_sensitive=False),
)
def update_app_authorization_rule(
    account_name: str,
    app_name: str,
    user: Optional[str],
    user_group: Optional[str],
    role: str,
) -> None:
    """Update app authorization rule for user/user group in app.

    Args:
        account_name: account to be updated.
        app_name: app to be updated.
        user: the user to apply new rules.
        user_group: the user group to apply new rules.
        role: role for the user/user group in the app (ADMIN, WRITER OR READER).
    """
    authorization_role = role.upper()
    api = AppAPI()
    try:
        api.update_app_authorization_rule(
            account_name,
            app_name,
            user,
            user_group,
            authorization_role,
        )
        subject = f"user `{user}`" if user is not None else f"user group `{user_group}`"
        write_console(
            f"Successfully updated new authorization rule for {subject} in app "
            f"`{app_name}` within account `{account_name}` with role "
            f"`{authorization_role}`\n",
            0,
        )
    except (APIServerError, UnauthenticatedError) as e:
        write_console(f"{e}\n", 1)


@rule.command(
    "rm",
    help="""Remove authorization rule to the user in the app.

                \b
                ACCOUNT_NAME: account to be updated.
                APP_NAME: account to be updated.
            """,
)
@click.argument(
    "account_name",
    required=True,
    type=str,
)
@click.argument(
    "app_name",
    required=True,
    type=str,
)
@click.option(
    "-u",
    "--user",
    required=False,
    type=str,
    help="user to be get new rules.",
)
@click.option(
    "-ug",
    "--user-group",
    required=False,
    type=str,
    help="user group to be get new rules",
)
def remove_app_authorization_rule(
    account_name: str,
    app_name: str,
    user: Optional[str],
    user_group: Optional[str],
) -> None:
    """Remove authorization rule for user in app.

    Args:
        account_name: account to be updated.
        app_name: account to be updated.
        user: the user to be updated.
        user_group: the user group to be updated.
    """
    if user is None and user_group is None:
        write_console("Please provide either user or user group\n", 1)
        return

    api = AppAPI()
    try:
        api.remove_app_authorization_rule(account_name, app_name, user, user_group)
        subject = f"user `{user}`" if user is not None else f"user group `{user_group}`"
        write_console(
            f"Successfully removed authorization rule for {subject} in app "
            f"`{app_name}` within account `{account_name}`\n",
            0,
        )
    except (APIServerError, UnauthenticatedError) as e:
        write_console(f"{e}\n", 1)


@rule.command(
    "ls",
    help="""List app user authorization role.

        \b
        ACCOUNT_NAME: account to be selected.
        APP_NAME: app to be selected.
    """,
)
@click.argument(
    "account_name",
    required=True,
    type=str,
)
@click.argument(
    "app_name",
    required=True,
    type=str,
)
def list_app_authorization_rule(
    account_name: str,
    app_name: str,
) -> None:
    """List app user authorization role.

    Args:
        account_name: account to be selected.
        app_name: account to be selected.
    """
    api = AppAPI()
    try:
        app_rules = api.list_app_authorization_rule(account_name, app_name)
    except (APIServerError, UnauthenticatedError) as e:
        write_console(f"{e}\n", 1)

    if app_rules:
        app_name = app_rules.get("appId")
        authorization_rules = app_rules.get("authorizationRules")
        console = Console()
        table = Table(
            title=f"Rules of app '{app_name}'",
            show_header=False,
            show_edge=True,
        )

        table.add_row("User/Group", "Role")
        table.add_section()

        for current_app in authorization_rules:
            subject = current_app.get("subject")
            name = subject.get("email", None) or subject.get("name", None)
            table.add_row(name, current_app.get("role"))
        console.print(table)
    else:
        write_console("No app member found\n", 0)
