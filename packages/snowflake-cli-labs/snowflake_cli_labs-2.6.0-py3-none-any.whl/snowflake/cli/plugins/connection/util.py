# Copyright (c) 2024 Snowflake Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging

from click.exceptions import ClickException
from snowflake.connector import SnowflakeConnection
from snowflake.connector.cursor import DictCursor

LOCAL_DEPLOYMENT: str = "us-west-2"

log = logging.getLogger(__name__)

REGIONLESS_QUERY = """
    select value['value'] as REGIONLESS from table(flatten(
        input => parse_json(SYSTEM$BOOTSTRAP_DATA_REQUEST()),
        path => 'clientParamsInfo'
    )) where value['name'] = 'UI_SNOWSIGHT_ENABLE_REGIONLESS_REDIRECT';
"""


class MissingConnectionHostError(ClickException):
    def __init__(self, conn: SnowflakeConnection):
        super().__init__(
            f"The connection host ({conn.host}) was missing or not in "
            "the expected format "
            "(<account>.<deployment>.snowflakecomputing.com)"
        )


def is_regionless_redirect(conn: SnowflakeConnection) -> bool:
    """
    Determines if the deployment this connection refers to uses
    regionless URLs in Snowsight (/orgname/account) or regional URLs
    (/region/account). If we cannot determine the correct value we
    assume it's regionless, as this is true for most production deployments.
    """
    try:
        *_, cursor = conn.execute_string(REGIONLESS_QUERY, cursor_class=DictCursor)
        return cursor.fetchone()["REGIONLESS"].lower() == "true"
    except:
        # by default, assume that
        log.warning("Cannot determine regionless redirect; assuming True.")
        return True


def get_context(conn: SnowflakeConnection) -> str:
    """
    Determines the first part of the path in a Snowsight URL.
    This could be a region or it could be an organization, depending
    on whether or not the underlying deployment uses regionless URLs.
    """
    if is_regionless_redirect(conn):
        *_, cursor = conn.execute_string(
            f"select system$return_current_org_name()", cursor_class=DictCursor
        )
        return cursor.fetchone()["SYSTEM$RETURN_CURRENT_ORG_NAME()"]

    host_parts = conn.host.split(".")
    if host_parts[-1] == "local":
        return LOCAL_DEPLOYMENT

    if len(host_parts) == 6:
        return ".".join(host_parts[1:4])

    raise MissingConnectionHostError(conn)


def get_account(conn: SnowflakeConnection) -> str:
    """
    Determines the account that this connection refers to.
    """
    try:
        *_, cursor = conn.execute_string(
            f"select current_account_name()", cursor_class=DictCursor
        )
        return cursor.fetchone()["CURRENT_ACCOUNT_NAME()"].lower()
    except Exception as e:
        # try to extract the account from the connection information
        if conn.account:
            return conn.account

        if not conn.host:
            raise MissingConnectionHostError(conn)

        host_parts = conn.host.split(".")
        return host_parts[0]


def get_snowsight_host(conn: SnowflakeConnection) -> str:
    try:
        *_, cursor = conn.execute_string(
            f"select system$get_snowsight_host()", cursor_class=DictCursor
        )
        return cursor.fetchone()["SYSTEM$GET_SNOWSIGHT_HOST()"]
    except Exception as e:
        # if we cannot determine the host, assume we're on prod
        return "https://app.snowflake.com"


def make_snowsight_url(conn: SnowflakeConnection, path: str) -> str:
    """
    Returns a URL on the correct Snowsight instance for the connected account.
    The path that is passed in must already be properly URL-encoded, and
    can optionally contain a hash/fragment (e.g. #).

    See also identifier_for_url.
    """
    snowsight_host = get_snowsight_host(conn)
    deployment = get_context(conn)
    account = get_account(conn)
    path_with_slash = path if path.startswith("/") else f"/{path}"
    return f"{snowsight_host}/{deployment}/{account}{path_with_slash}"
