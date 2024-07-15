"""
Software Update

"""

from __future__ import annotations

from typing import Literal

from restfly import APIEndpoint
from restfly.utils import dict_clean


class SoftwareUpdateAPI(APIEndpoint):
    _path = "settings/software-update"

    def update(self) -> None:
        """
        Schedules a software update for all components

        Example:

            >>> nessus.software_update.update()
        """
        self._get()

    def settings(
        self,
        update: Literal["all", "plugins", "disabled"],
        custom_host: str | None = None,
        auto_update_delay: int | None = None,
    ) -> None:
        """
        Update the software update settings

        Args:
            update (str):
                What components should be updated?  Expected values are
                ``all``, ``plugins``, and ``disabled``.
            custom_host (str, optional):
                URL of the custom plugin feed host
            auto_update_delay (int, optional):
                How often should the plugin feed attempt to update (in hours)

        Example:

            >>> nessus.software_update.settings(update='all',
            ...                                 auto_update_delay=24
            ...                                 )
        """
        self._put(
            json=dict_clean({"update": update, "custom_host": custom_host, "auto_update_delay": auto_update_delay})
        )
