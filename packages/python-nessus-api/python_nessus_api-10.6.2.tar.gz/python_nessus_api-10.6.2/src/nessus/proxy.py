"""
Proxy
"""

from __future__ import annotations

from typing import Dict, Literal, Optional

from restfly import APIEndpoint
from restfly.utils import dict_clean


class ProxyAPI(APIEndpoint):
    _path = "settings/network/proxy"

    def edit(
        self,
        proxy: str | None = None,
        proxy_auth: Literal["auto", "basic", "digest", "none", "ntlm"] | None = None,
        proxy_password: str | None = None,
        proxy_port: int | None = None,
        proxy_username: str | None = None,
        user_agent: str | None = None,
    ) -> None:
        """
        Updates the proxy settings.

        Args:
            proxy (str, optional): The proxy host
            proxy_auth (str, optional): The proxy auth method
            proxy_password (str, optional): The auth password
            proxy_port (int, optional): The proxy port
            proxy_username (str, optional): The proxy auth username
            user_agent (str, optional): The proxy user agent.

        Example:

            >>> nessus.proxy.edit(proxy='proxy.company.com',
            ...                   proxy_auth='none',
            ...                   proxy_port=3128
            ...                   )
        """
        self._put(
            json=dict_clean(
                {
                    "proxy": proxy,
                    "proxy_auth": proxy_auth,
                    "proxy_password": proxy_password,
                    "proxy_port": proxy_port,
                    "proxy_username": proxy_username,
                    "user_agent": user_agent,
                }
            )
        )

    def details(self) -> dict:
        """
        Retrieves the current proxy settings

        Returns:
            Dict:
                The current proxy settings

        Example:

            >>> nessus.proxy.details()
        """
        return self._get()
