"""
Migration
"""

from __future__ import annotations

from typing import Dict, List, Literal

from restfly import APIEndpoint
from restfly.utils import dict_clean


class MigrationAPI(APIEndpoint):
    _path = "migration"

    def get_settings(self) -> dict:
        """
        Returns the current migration settings

        Returns:


        Example:

            >>> nessus.migration.get_settings()
        """
        return self._get("config")

    def update_settings(self, key: str, secret: str, domain: str) -> None:
        """
        Changes the migration settings.

        Example:

            >>> nessus.migration.update_settings()
        """
        return self._put(
            "config",
            params=dict_clean({"key": key, "secret": secret, "domain": domain}),
        )

    def status(self) -> dict:
        """
        Returns the migration status.

        Example:

            >>> nessus.migration.status()
        """
        return self._get()

    def start(self) -> None:
        """
        Starts or resumes the migration. Before you start the migration, you need have the 'key', 'secret' and 'domain' settings set

        Example:

            >>> nessus.migration.start()
        """
        self._post()

    def stop(self, finish: bool) -> None:
        """
        Finishes or stops the migration.

        Args:
            finish (bool): If true, finish the migration; otherwise, cancel the migration

        Example:

            >>> nessus.migration.stop()
        """
        self._delete(params=dict_clean({"finish": finish}))

    def scan_history(self, object_type: Literal["scanner"], object_id: int, acls: list[dict]) -> None:
        """
        Updates the permissions for the specified object

        Args:
            object_type (str): The type of object to modify
            object_id (int): The unique id of the object to modify
            acls (list[dict]): The list of access control objects to apply

        Example:

            >>> nessus.permissions.edit('scanner', 1, acls=[
            ...     {
            ...         'type': 'default',
            ...         'permissions': 16
            ...     }, {
            ...         'type': 'user',
            ...         'permissions': 64,
            ...         'name': 'admin',
            ...         'id': 1,
            ...         'owner': 1
            ...     })
        """
        self._put(f"{object_type}/{object_id}", json={"acls": acls})

    def scan_history_settings(self) -> dict:
        """
        Returns the current scan history migration settings.

        Example:

            >>> nessus.migration.scan_history_settings()
        """
        self._get(f"scan-history/upload-settings")

    def update_scan_history_settings(
        self,
        days_of_history: int,
        concurrent_uploads: int = 1,
        seconds_to_sleep_between_each_upload: int = 0,
    ) -> None:
        """
        Changes the scan history migration settings.

        Args:
            days_of_history (int): The days of scan history to migrate. 0 means migrate all the scan histories.
            concurrent_uploads (int): The concurrent number of scan histories to migrate. Default is 1.
            seconds_to_sleep_between_each_upload (int): The number of seconds to pause after one item finished migration. Default is 0.

        Example:

            >>> nessus.permissions.update_scan_history_settings()
        """
        self._post(
            f"scan-history/upload-settings",
            json={
                "settings": {
                    "days_of_history": days_of_history,
                    "concurrent_uploads": concurrent_uploads,
                    "seconds_to_sleep_between_each_upload": seconds_to_sleep_between_each_upload,
                }
            },
        )

    def start_scan_history_migration(self, object_type: Literal["scanner"], object_id: int, acls: list[dict]) -> None:
        """
        Updates the permissions for the specified object

        Args:
            object_type (str): The type of object to modify
            object_id (int): The unique id of the object to modify
            acls (list[dict]): The list of access control objects to apply

        Example:

            >>> nessus.permissions.edit('scanner', 1, acls=[
            ...     {
            ...         'type': 'default',
            ...         'permissions': 16
            ...     }, {
            ...         'type': 'user',
            ...         'permissions': 64,
            ...         'name': 'admin',
            ...         'id': 1,
            ...         'owner': 1
            ...     })
        """
        self._put(f"{object_type}/{object_id}", json={"acls": acls})

    def stop_scan_history_migration(self, object_type: Literal["scanner"], object_id: int, acls: list[dict]) -> None:
        """
        Updates the permissions for the specified object

        Args:
            object_type (str): The type of object to modify
            object_id (int): The unique id of the object to modify
            acls (list[dict]): The list of access control objects to apply

        Example:

            >>> nessus.permissions.edit('scanner', 1, acls=[
            ...     {
            ...         'type': 'default',
            ...         'permissions': 16
            ...     }, {
            ...         'type': 'user',
            ...         'permissions': 64,
            ...         'name': 'admin',
            ...         'id': 1,
            ...         'owner': 1
            ...     })
        """
        self._put(f"{object_type}/{object_id}", json={"acls": acls})

    def skip_scan_history(self, scan_uuid: str) -> None:
        """
        Skips migrating a single scan history item.

        Args:
            scan_uuid (str): The uuid of the scan history item to skip.

        Example:

            >>> nessus.migration.skip_scan_history()
        """
        self._post(f"scan-history/{scan_uuid}/skip-upload")

    def skip_scan_history_bulk(self, ids: list[str]) -> None:
        """
        Skips migrating scan history items in bulk.

        Args:
            ids (list[str]): Array of scan history uuids to skip.

        Example:

            >>> nessus.migration.skip_scan_history_bulk()
        """
        self._post(f"scan-history/skip-upload", param={"ids": ids})

    def reset_scan_history(self, scan_uuid: str) -> None:
        """
        Resets a scan history item's status to 'not started' so it will be migrated.

        Args:
            scan_uuid (str): The uuid of the scan history item to reset.

        Example:

            >>> nessus.migration.reset_scan_history()
        """
        self._post(f"scan-history/{scan_uuid}/start-upload")

    def reset_scan_history_bulk(self, ids: list[str]) -> None:
        """
        Resets the status of the scan history items matching the provided IDs so they can be migrated.

        Args:
            ids (array): Array of scan history item uuids to reset.

        Example:

            >>> nessus.migration.reset_scan_history_bulk()

        """
        self._post(f"scan-history/start-upload", param={"ids": ids})
