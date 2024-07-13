"""
Mail
"""

from __future__ import annotations

from typing import Dict, Literal, Optional

from restfly import APIEndpoint
from restfly.utils import dict_clean, dict_merge


class MailAPI(APIEndpoint):
    _path = "settings/network/mail"

    def details(self) -> dict:
        """
        Retrieves the Nessus daemon's mail settings.

        Returns:
            Dict:
                Dictionary of SMTP settings

        Example:

            >>> nessus.mail.details()
        """
        return self._get()

    def edit(
        self,
        smtp_host: str | None = None,
        smtp_port: int | None = None,
        smtp_enc: None | (
            Literal["No Encryption", "Use TLS if available", "Force SSL" "Force TLS"]
        ) = None,
        smtp_from: str | None = None,
        smtp_www_host: str | None = None,
        smtp_user: str | None = None,
        smtp_pass: str | None = None,
        smtp_auth: None | (
            Literal["NONE", "PLAIN", "LOGIN", "NTLM", "CRAM-MD5"]
        ) = None,
    ) -> None:
        """
        Updates the Nessus daemon's mail settings

        Args:
            smtp_host (str, optional):
                DNS/IP Address of the SMTP server
            smtp_port (int, optional):
                Port number for the SMTP service
            smtp_enc (str, optional):
                The connection encryption for the SMTP server
            smtp_from (str, optional):
                Reply email address for email sent by the Nessus daemon
            smtp_www_host (str, optional):
                The host to use in email links
            smtp_user (str, optional):
                The username to use when authenticating to the SMTP service
            smtp_pass (str, optional):
                The password to use when authenticating to the SMTP service
            smtp_auth (str, optional):
                The authentication type for the SMTP server

        Example:

            >>> nessus.mail.edit(smtp_user='new_user',
            ...                  smtp_pass='updated_password',
            ...                  smtp_auth='LOGIN',
            ...                  )
        """
        current = self.details()
        updated = dict_merge(
            current,
            dict_clean(
                {
                    "smtp_host": smtp_host,
                    "smtp_port": smtp_port,
                    "smtp_enc": smtp_enc,
                    "smtp_from": smtp_from,
                    "smtp_www_host": smtp_www_host,
                    "smtp_user": smtp_user,
                    "smtp_pass": smtp_pass,
                    "smtp_auth": smtp_auth,
                }
            ),
        )
        self._put(json=updated)
