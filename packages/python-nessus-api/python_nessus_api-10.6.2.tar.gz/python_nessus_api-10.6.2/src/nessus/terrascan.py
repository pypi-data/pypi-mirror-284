"""
Terrascan
"""

from __future__ import annotations

import time
from io import BytesIO
from typing import Callable, Dict, List, Literal, Optional

from requests import Response
from restfly import APIEndpoint
from restfly.utils import dict_clean

from .utils import *


class TerrascanAPI(APIEndpoint):
    _path = "tools/terrascan"

    def get_info(self) -> None:
        """
        Returns information about Terrascan

        Example:

            >>> nessus.terrascan.get_info()
        """
        return self._get()

    def set_desired(self) -> None:
        """
        Set whether to install or remove Terrascan.

        Args:
            terrascan_desired (boolean): Set to true if Terrascan should be installed, otherwise set to false

        Example:

            >>> nessus.terrascan.set_desired(True)
        """
        self._post()

    def download(self) -> None:
        """
        Download Terrascan

        Example:

            >>> nessus.terrascan.download()
        """
        self._post("download")

    def get_config(self, config_id: int) -> dict:
        """
        Get a configuration.

        Args:
            config_id (int): The config id to get

        Example:

            >>> nessus.terrascan.get_config(config_id)
        """
        return self._get(f"configs/{config_id}")

    def save_config(self, config: dict, name: str, config_id: int) -> dict:
        """
        Save a configuration.

        Args:
            config (json): The configuration
            name (str): The configuration name
            config_id (int): The configuration id to save

        Example:

            >>> nessus.terrascan.save_config(config, 'Example name', config_id)
        """
        return self._post()

    def delete_config(self, config_id: int) -> None:
        """
        Delete a configuration.

        Args:
            config_id (int): The config id to delete

        Example:

            >>> nessus.terrascan.delete_config(config_id)
        """
        self._delete(f"configs/{config_id}")

    def edit_config(self, config_id: int) -> None:
        """
        Edit a configuration.

        Args:
            config_id (int): The config id to edit

        Example:

            >>> nessus.terrascan.edit_config(config_id)
        """
        self._put(f"configs/{config_id}")

    def get_configs(self) -> list[dict]:
        """
        Get list of configurations.

        Example:

            >>> nessus.terrascan.get_configs()
        """
        return self._get(f"configs")

    def delete_configs(self):
        """
        Set whether to install or remove Terrascan.

        Args:
            group_id (int): The agent group id to modify
            name (str): The name of the agent group

        Example:

            >>> nessus.terrascan.set_desired(group_id, 'Example name')
        """

    def get_default_config(self):
        """
        Get default configuration.



        Example:

            >>> nessus.terrascan.get_default_config()
        """

    def get_scans(self, config_id: int) -> list:
        """
        List of Terrascan scans.

        Args:
            config_id (int): Configuration id

        Returns:
            List:
                The status response
        Example:

            >>> nessus.terrascan.get_scans(scan_id)
        """
        self._get(f"scans/{config_id}")

    def launch_scan(self, config_id: int) -> None:
        """
        Launch Terrascan scans.

        Args:
            config_id (int): Configuration id to be launch

        Example:

            >>> nessus.terrascan.launch_scan(scan_id)
        """
        self._post(f"scans/{config_id}")

    def delete_scan(self, scan_ids: list[int]) -> None:
        """
        Delete Terrascan scans.

        Args:
            scan_id (List[int]): List of scan ids to be delete

        Example:

            >>> nessus.terrascan.delete_scan(scan_ids)
        """
        self._delete("scan", json={"scan_ids": scan_ids})

    def download_scan_result(self, config_id: int, scan_id: int, format: str) -> dict:
        """
        Download Terrascan scan results.

        Args:
            config_id (int): The configuration id
            scan_id (int): The scan id
            format (str): Desired format

        Example:

            >>> nessus.terrascan.download_scan_result(config_id, scan_id, 'format')
        """
        return self._get(f"scan/results/{config_id}/{scan_id}/{format}")

    def dowload_scan_result_command_result(self, config_id: int, scan_id: int) -> dict:
        """
        Download Terrascan scan result command output.

        Args:
            config_id (int): The configuration id
            scan_id (int): The scan id

        Example:

            >>> nessus.terrascan.dowload_scan_result_command_result(config_id, scan_id)
        """
        return self._get(f"scan/command_output/{config_id}/{scan_id}")
