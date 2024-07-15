"""
Scanners
"""

from __future__ import annotations

from typing import Literal

from restfly import APIEndpoint
from restfly.utils import dict_clean


class ScannersAPI(APIEndpoint):
    _path = "scanners"

    def control_scan(self, scanner_id: int, scan_uuid: str, action: Literal["stop", "pause", "resume"]) -> None:
        """
        Controls a scan currently running on a scanner.

        Args:
            scanner_id (int): Id of the scanner to control
            scan_uuid (str): UUID of the scan to control
            action (str): The action to perform on the scan.

        Example:

            >>> nessus.scanners.control_scan(scanner_id, scan_uuid, 'pause')
        """
        self._post(f"{scanner_id}/scans/{scan_uuid}/control", json={"action": action})

    def delete(self, scanner_id: int) -> None:
        """
        Delete and unlink the scanner.

        Args:
            scanner_id (int): Id of the scanner to delete

        Example:

            >>> nessus.scanners.delete(1)
        """
        self._delete(f"{scanner_id}")

    def delete_many(self, scanner_ids: list[int]) -> None:
        """
        Delete and unlink many scanners.

        Args:
            scanner_ids (list[int]): List of scanner ids to delete

        Example:

            >>> nessus.scanners.delete_many([1, 2, 3])
        """
        self._delete(json={"ids": scanner_ids})

    def details(self, scanner_id: int) -> dict:
        """
        Retrieve the details for a scanner.

        Args:
            scanner_id (int): Id of the scanner to retrieve

        Example:

            >>> nessus.scanners.details(1)
        """
        return self._get(f"{scanner_id}")

    def update(
        self,
        scanner_id: int,
        force_plugin_update: int | None = None,
        force_ui_update: int | None = None,
        finish_update: int | None = None,
        registration_code: str | None = None,
        aws_update_interval: int | None = None,
    ) -> None:
        """
        Update the scanner

        Args:
            scanner_id (int):
                Id of the scanner to update
            force_plugin_update (int, optional):
                Pass 1 to force a plugin update.
            force_ui_update (int, optional):
                Pass 1 to force a UI update.
            finish_update (int, optional):
                Pass 1 to reboot the scanner and run the latest software update
                (only valid if automatic updates are disabled).
            registration_code (str, optional):
                Sets the registration code for the scanner.
            aws_update_interval (int, optional):
                Informs the scanner how often to check into the controlling
                Nessus service.  This is only valid for AWS scanners.

        Example:

            >>> nessus.scanners.update(1,
            ...                        force_plugin_update=True,
            ...                        force_ui_update=True
            ...                        )
        """
        self._put(
            f"{scanner_id}",
            json=dict_clean(
                {
                    "force_plugin_update": force_plugin_update,
                    "force_ui_update": force_ui_update,
                    "finish_update": finish_update,
                    "registration_code": registration_code,
                    "aws_update_interval": aws_update_interval,
                }
            ),
        )

    def aws_targets(self, scanner_id: int) -> list[dict]:
        """
        Retrieves the AWS targets from the scanner.  Only applies to AWS
        scanners.

        Args:
            scanner_id (int): Id of the scanner to call

        Returns:
            List:
                List of AWS target objects.

        Example:

            >>> for target in nessus.scanners.aws_targets(1):
            ...     print(target)
        """
        return self._get(f"{scanner_id}/aws-targets")["targets"]

    def scanner_key(self, scanner_id: int) -> str:
        """
        Retrieves the scanner key for the requested scanner.

        Args:
            scanner_id (int): Id of the scanner to call

        Returns:
            str:
                The scanner key

        Example:

            >>> nessus.scanners.scanner_key(1)
        """
        return self._get(f"{scanner_id}/key")["key"]

    def running_scans(self, scanner_id: int) -> list[dict]:
        """
        Retrieves the list of running scans on the scanner.

        Args:
            scanner_id (int): Id of the scanner to call

        Returns:
            List:
                If scans are running on the scanner, a list of scan objects
                will be returned.  If no scans are currently running on the
                scanner, then a None object will be returned.

        Example:

            >>> scans = nessus.scanners.active_scans(1)
            >>> if scans:
            ...     for scan in scans:
            ...         print(scan)
        """
        return self._get(f"{scanner_id}/scans")["scans"]

    def list(self) -> list[dict]:
        """
        Returns a list of scanners.

        Returns:
            List:
                List of scanners connected to this scanner.

        Example:

            >>> for scanner in nessus.scanners.list():
            ...     print(scanner)
        """
        return self._get()["scanners"]

    def link_state(self, scanner_id: int, linked: bool) -> None:
        """
        Toggles the link state of the specified scanner.

        Args:
            scanner_id (int): Id of the scanner to modify
            linked (bool): Should the scanner be linked?

        Example:

            >>> nessus.scanners.link_state(1, linked=True)
        """
        self._put(f"{scanner_id}/link", json={"link": int(linked)})
