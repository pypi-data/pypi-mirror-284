"""
Nessus
"""

from __future__ import annotations

import os
import re
import warnings

from restfly import APISession

from .agent_groups import AgentGroupsAPI
from .agents import AgentsAPI
from .editor import EditorAPI
from .file import FileAPI
from .folders import FoldersAPI
from .groups import GroupsAPI
from .mail import MailAPI
from .migration import MigrationAPI
from .permissions import PermissionsAPI
from .plugin_rules import PluginRulesAPI
from .plugins import PluginsAPI
from .policies import PoliciesAPI
from .proxy import ProxyAPI
from .scanners import ScannersAPI
from .scans import ScansAPI
from .server import ServerAPI
from .session import SessionAPI
from .settings import SettingsAPI
from .software_update import SoftwareUpdateAPI
from .terrascan import TerrascanAPI
from .tokens import TokensAPI
from .users import UsersAPI
from .utils import url_validator


class Nessus(APISession):
    _lib_name = "nessus"
    _lib_version = "10.6.1"
    _backoff = 1
    _retries = 3
    _auth_mech = None
    _ssl_verify = False
    _conv_json = True

    def __init__(self, **kwargs):
        self._url = kwargs.get("url", os.environ.get(f"NESSUS_URL", self._url))
        if not url_validator(self._url):
            raise TypeError(f"{self._url} is not a valid URL")
        super().__init__(**kwargs)

    def _session_auth(self, username, password):

        token = self.post("session", json={"username": username, "password": password}).get("token")
        self._session.headers.update({"X-Cookie": f"token={token}"})
        x_api_token = None
        pattern = (
            r"\{key:\"getApiToken\",value:function\(\)\{"
            r"return\"([a-zA-Z0-9]*-[a-zA-Z0-9]*-[a-zA-Z0-9]*-"
            r"[a-zA-Z0-9]*-[a-zA-Z0-9]*)\"\}"
        )
        response = self.get("nessus6.js")
        if response.status_code == 200:
            matched = re.search(pattern, str(response.content))
            if matched:
                x_api_token = matched.group(1)
        self._session.headers.update({"X-API-Token": x_api_token})

    def _authenticate(self, **kwargs):
        """
        This method handles authentication for both API Keys and for session
        authentication.
        """
        self._auth = kwargs.get(
            "_session_auth_dict",
            {
                "username": kwargs.get("username", os.getenv("NESSUS_USERNAME")),
                "password": kwargs.get("password", os.getenv("NESSUS_PASSWORD")),
            },
        )

        if None not in [v for _, v in self._auth.items()]:
            self._session_auth(**self._auth)
        else:
            warnings.warn(
                "Starting an unauthenticated session",
            )
            self._log.warning("Starting an unauthenticated session.")

    def _deauthenticate(self, method: str = "DELETE", path: str = "session"):
        """
        This method handles de-authentication.  This is only necessary for
        session-based authentication.
        """
        if self._auth_mech == "user":
            self._req(method, path)
        self._auth = {}
        self._auth_mech = None

    @property
    def agent_groups(self):
        """
        The interface object for the
        :doc:`Nessus Agent Groups APIs <agent_groups>`.
        """
        return AgentGroupsAPI(self)

    @property
    def agents(self):
        """
        The interface object for the :doc:`Nessus Agents APIs <agents>`.
        """
        return AgentsAPI(self)

    @property
    def editor(self):
        """
        The interface object for the :doc:`Nessus Editor APIs <editor>`.
        """
        return EditorAPI(self)

    @property
    def file(self):
        """
        The interface object for the :doc:`Nessus File APIs <files>`.
        """
        return FileAPI(self)

    @property
    def folders(self):
        """
        The interface object for the :doc:`Nessus Folders APIs <folders>`.
        """
        return FoldersAPI(self)

    @property
    def groups(self):
        """
        The interface object for the :doc:`Nessus Groups APIs <groups>`.
        """
        return GroupsAPI(self)

    @property
    def mail(self):
        """
        The interface object for the :doc:`Nessus Mail APIs <mail>`.
        """
        return MailAPI(self)

    @property
    def migration(self):
        """
        The interface object for the :doc:`Nessus Migration APIs <migration>`.
        """
        return MigrationAPI(self)

    @property
    def permissions(self):
        """
        The interface object for the
        :doc:`Nessus Permissions APIs <permissions>`.
        """
        return PermissionsAPI(self)

    @property
    def plugin_rules(self):
        """
        The interface object for the
        :doc:`Nessus Plugin Rules APIs <plugin_rules>`.
        """
        return PluginRulesAPI(self)

    @property
    def plugins(self):
        """
        The interface object for the :doc:`Nessus Plugins APIs <plugins>`.
        """
        return PluginsAPI(self)

    @property
    def policies(self):
        """
        The interface object for the :doc:`Nessus Policies APIs <policies>`.
        """
        return PoliciesAPI(self)

    @property
    def proxy(self):
        """
        The interface object for the :doc:`Nessus Proxy APIs <proxy>`.
        """
        return ProxyAPI(self)

    @property
    def scanners(self):
        """
        The interface object for the :doc:`Nessus Scanners APIs <scanners>`.
        """
        return ScannersAPI(self)

    @property
    def scans(self):
        """
        The interface object for the :doc:`Nessus Scans APIs <scans>`.
        """
        return ScansAPI(self)

    @property
    def server(self):
        """
        The interface object for the :doc:`Nessus Server APIs <server>`.
        """
        return ServerAPI(self)

    @property
    def session(self):
        """
        The interface object for the :doc:`Nessus Session APIs <session>`.
        """
        return SessionAPI(self)

    @property
    def settings(self):
        """
        The interface object for the :doc:`Nessus Settings APIs <settings>`.
        """
        return SettingsAPI(self)

    @property
    def software_update(self):
        """
        The interface object for the
        :doc:`Nessus Software Update APIs <software_update>`.
        """
        return SoftwareUpdateAPI(self)

    @property
    def terrascan(self):
        return TerrascanAPI(self)

    @property
    def tokens(self):
        """
        The interface object for the :doc:`Nessus Tokens APIs <tokens>`.
        """
        return TokensAPI(self)

    @property
    def users(self):
        """
        The unterface object for the :doc:`Nessus Users APIs <users>`.
        """
        return UsersAPI(self)
