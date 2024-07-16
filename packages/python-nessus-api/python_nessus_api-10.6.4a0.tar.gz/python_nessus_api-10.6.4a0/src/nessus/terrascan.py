"""
Terrascan
"""

from __future__ import annotations

from restfly import APIEndpoint
from restfly.utils import dict_clean


class TerrascanAPI(APIEndpoint):
    _path = "tools/terrascan"

    def get_info(self) -> dict:
        """
        Returns information about Terrascan

        Example:

            >>> nessus.terrascan.get_info()
        """
        return self._get()

    def set_desired(self, terrascan: bool) -> None:
        """
        Set whether to install or remove Terrascan.

        Args:
            terrascan (boolean): Set to true if Terrascan should be installed, otherwise set to false

        Example:

            >>> nessus.terrascan.set_desired(True)
        """
        self._post(params={"terrascan": terrascan})

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

    def save_config(self, config: dict, name: str, config_id: int | None = None) -> None:
        """
        Save a configuration.

        Args:
            config (json): The configuration
            name (str): The configuration name
            config_id (int, optional): The configuration id to save

        Example:

            >>> nessus.terrascan.save_config(config, 'Example name', 1)
        """
        self._post("configs", params=dict_clean({"config": config, "name": name, "config_id": config_id}))

    def delete_config(self, config_id: int) -> None:
        """
        Delete a configuration.

        Args:
            config_id (int): The config id to delete

        Example:

            >>> nessus.terrascan.delete_config(1)
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

    def get_configs(self) -> None:
        """
        Get list of configurations.

        Example:

            >>> nessus.terrascan.get_configs()
        """
        self._get("configs")

    def delete_configs(self, config_id: int) -> None:
        """
        Delete configurations.

        Args:
            config_id (int): The config id to delete

        Example:

            >>> nessus.terrascan.delete_config(1)
        """
        self._delete(f"configs/{config_id}")

    def get_default_config(self) -> dict:
        """
        Get default configuration.

        Example:

            >>> nessus.terrascan.get_default_config()
        """
        return self._get("configs/default")

    def get_scans(self, config_id: int) -> None:
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
        self._delete("scan", params={"scan_ids": scan_ids})

    def download_scan_result(self, config_id: int, scan_id: int, format: str) -> None:
        """
        Download Terrascan scan results.

        Args:
            config_id (int): The configuration id
            scan_id (int): The scan id
            format (str): Desired format

        Example:

            >>> nessus.terrascan.download_scan_result(config_id, scan_id, 'format')
        """
        self._get(f"scan/results/{config_id}/{scan_id}/{format}")

    def dowload_scan_result_command_output(self, config_id: int, scan_id: int) -> None:
        """
        Download Terrascan scan result command output.

        Args:
            config_id (int): The configuration id
            scan_id (int): The scan id

        Example:

            >>> nessus.terrascan.dowload_scan_result_command_result(config_id, scan_id)
        """
        self._get(f"scan/command_output/{config_id}/{scan_id}")
