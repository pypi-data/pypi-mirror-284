"""app command for engineai CLI."""

import click
from rich.console import Console
from rich.table import Table

from engineai.sdk.cli.utils import write_console
from engineai.sdk.dashboard.clients.api import DashboardAPI
from engineai.sdk.dashboard.clients.mutation.app_api import AppAPI
from engineai.sdk.internal.clients.exceptions import APIServerError
from engineai.sdk.internal.exceptions import UnauthenticatedError

from .app_rule import rule


@click.group(name="app", invoke_without_command=False)
def app() -> None:
    """App commands."""


@app.command(
    "ls",
    help="""List all apps.

            \b
            Args:
                ACCOUNT_NAME: account to be listed.
            """,
)
@click.argument(
    "account_name",
    required=True,
    type=str,
)
def list_account_app(account_name: str) -> None:
    """List account apps.

    Args:
        account_name: account to be listed.
    """
    api = DashboardAPI()
    try:
        apps = api.list_account_apps(account_name)
    except (APIServerError, UnauthenticatedError) as e:
        write_console(f"{e}\n", 1)

    if apps:
        slug = apps.get("slug")
        account_apps = apps.get("apps", [])
        console = Console()
        table = Table(
            title=f"Apps of account '{slug}'",
            show_header=False,
            show_edge=True,
        )
        for current_app in account_apps:
            table.add_row(current_app.get("appId"))
        console.print(table)
    else:
        write_console("No apps found\n", 0)


@app.command(
    "add",
    help="""Add new app.

            \b
            Args:
                ACCOUNT_NAME: account to be added.
                APP_NAME: app to be added.
                TITLE: app title.
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
@click.argument(
    "title",
    required=True,
    type=str,
)
def add_app(account_name: str, app_name: str, title: str) -> None:
    """Add new app.

    Args:
        account_name: account to be added.
        app_name: app to be added.
        title: app title.
    """
    api = AppAPI()

    try:
        api.create_app(account_name, app_name, title)
        write_console(
            f"Successfully created app `{app_name}` within account "
            f"`{account_name}`\n",
            0,
        )
    except (APIServerError, UnauthenticatedError) as e:
        write_console(f"{e}\n", 1)


@app.command(
    "rename",
    help="""Update current app.

        \b
        Args:
            ACCOUNT_NAME: account to be updated.
            APP_NAME: app to be updated.
            NEW_APP_NAME: new app name.
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
@click.argument(
    "new_app_name",
    required=True,
    type=str,
)
def update(account_name: str, app_name: str, new_app_name: str) -> None:
    """Update current app.

    Args:
        account_name: account to be updated.
        app_name: app to be updated.
        new_app_name: new app name.
    """
    api = AppAPI()
    try:
        api.update_app(account_name, app_name, new_app_name)
        write_console(
            f"Successfully renamed app `{app_name}` within the Account "
            f"`{account_name}` to `{new_app_name}`\n",
            0,
        )
    except (APIServerError, UnauthenticatedError) as e:
        write_console(f"{e}\n", 1)


app.add_command(rule)
