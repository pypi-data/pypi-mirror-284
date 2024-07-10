"""Helper class to connect to APP API and obtain base types."""

import logging
from typing import Any
from typing import List
from typing import Optional

from engineai.sdk.internal.clients import APIClient

logger = logging.getLogger(__name__)
logging.getLogger("urllib3").propagate = False


class AppAPI(APIClient):
    """App API class."""

    def create_app(self, account_name: str, app_name: str, title: str) -> Any:
        """Create App."""
        return self._request(
            query="""
                mutation CreateApp($input: CreateAppInput!) {
                    createApp(input: $input) {
                        app {
                            appId
                            slug
                        }
                    }
                }""",
            variables={
                "input": {"accountSlug": account_name, "slug": app_name, "title": title}
            },
        )

    def update_app(self, account_name: str, app_name: str, new_app_name: str) -> Any:
        """Update App."""
        return self._request(
            query="""
                mutation UpdateApp($input: UpdateAppInput!) {
                    updateApp(input: $input) {
                        app {
                            appId
                        }
                    }
                }
                """,
            variables={
                "input": {
                    "accountSlug": account_name,
                    "slug": app_name,
                    "newSlug": new_app_name,
                }
            },
        )

    def add_app_authorization_rule(
        self,
        account_name: str,
        app_name: str,
        user: Optional[str],
        user_group: Optional[str],
        role: str,
    ) -> List:
        """Add authorization rule for member or group in the app."""
        return self._request(
            query="""
                mutation addAuthorizationRule($input: AddAppAuthorizationRuleInput!){
                    addAppAuthorizationRule(input: $input) {
                        rule {
                            app {
                                appId
                                account {
                                    slug
                                }
                            }
                            role
                            subject{
                                ... on User {
                                    email
                                }
                                ... on UserGroup {
                                    name
                                }
                            }
                        }
                    }
                }""",
            variables={
                "input": {
                    "accountSlug": account_name,
                    "appSlug": app_name,
                    "subject": (
                        {"userEmail": user}
                        if user is not None
                        else {"groupSlug": user_group}
                    ),
                    "role": role,
                }
            },
        ).get("data", {})

    def update_app_authorization_rule(
        self,
        account_name: str,
        app_name: str,
        user: Optional[str],
        user_group: Optional[str],
        role: str,
    ) -> List:
        """Update authorization rule for member or group in the app."""
        return self._request(
            query="""
                mutation updateAuthorizationRule
                ($input: UpdateAppAuthorizationRuleInput!){
                    updateAppAuthorizationRule(input: $input) {
                        rule {
                            app {
                                appId
                                account {
                                    slug
                                }
                            }
                            role
                            subject{
                                ... on User {
                                    email
                                }
                                ... on UserGroup {
                                    name
                                }
                            }
                        }
                    }
                }""",
            variables={
                "input": {
                    "accountSlug": account_name,
                    "appSlug": app_name,
                    "subject": (
                        {"userEmail": user}
                        if user is not None
                        else {"groupSlug": user_group}
                    ),
                    "role": role,
                }
            },
        ).get("data", {})

    def remove_app_authorization_rule(
        self,
        account_name: str,
        app_name: str,
        user: Optional[str],
        user_group: Optional[str],
    ) -> List:
        """Remove account member."""
        return self._request(
            query="""
                mutation removeAuthorizationRule
                ($input: RemoveAppAuthorizationRuleInput!){
                    removeAppAuthorizationRule(input: $input) {
                        rule {
                            app {
                                appId
                                account {
                                    slug
                                }
                            }
                            role
                            subject{
                                ... on User {
                                    email
                                }
                                ... on UserGroup {
                                    name
                                }
                            }
                        }
                    }
                }""",
            variables={
                "input": {
                    "accountSlug": account_name,
                    "appSlug": app_name,
                    "subject": (
                        {"userEmail": user}
                        if user is not None
                        else {"groupSlug": user_group}
                    ),
                }
            },
        ).get("data", {})

    def list_app_authorization_rule(
        self,
        account_name: str,
        app_name: str,
    ) -> List:
        """List all apps authorization rules."""
        return (
            (
                self._request(
                    query="""
                        query ListAppRules($appId: String, $accountSlug: String){
                            app(appId: $appId, accountSlug: $accountSlug) {
                                account {
                                    slug
                                }
                                appId
                                authorizationRules {
                                    role
                                    subject{
                                        ... on User {
                                            email
                                        }
                                        ... on UserGroup {
                                            name
                                        }
                                    }
                                }
                            }
                        }""",
                    variables={"accountSlug": account_name, "appId": app_name},
                )
            )
            .get("data", {})
            .get("app", {})
        )
