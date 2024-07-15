"""
Permissions
"""

from __future__ import annotations

from typing import Literal

from restfly import APIEndpoint


class PermissionsAPI(APIEndpoint):
    _path = "permissions"

    def details(self, object_type: Literal["scanner"], object_id: int) -> list[dict]:
        """
        Retrieves the access control list for the specified object.

        Args:
            object_type (str): The type of permissions object
            object_id (int): The unique id of the object to retrieve

        Returns:
            List:
                List of ACL objects.

        Example:

            >>> nessus.permissions.details('scanner', 1)
        """
        return self._get(f"{object_type}/{object_id}")

    def edit(self, object_type: Literal["scanner"], object_id: int, acls: list[dict]) -> None:
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
