"""
Agents
"""

from __future__ import annotations

from typing import Dict, List, Literal, Optional, Tuple, Union

from restfly import APIEndpoint

from .iterators.pagination import PaginationIterator
from .schema.pagination import ListSchema


class AgentsAPI(APIEndpoint):
    """
    Agent
    """

    _path = "agents"

    def delete(self, agent_id: int) -> None:
        """
        Deletes an agent.

        Args:
            agent_id (int): Id of the agent to delete

        Example:

            >>> nessus.agents.delete(agent_id)
        """
        self._delete(f"{agent_id}")

    def delete_bulk(self, agent_ids: list[int]) -> None:
        """
        Deletes multiple agents.

        Args:
            agent_ids (list[int]): List of agent ids to delete

        Example:

            >>> nessus.agents.delete_many([agent1, agent2, agent3])
        """
        self._delete(json={"ids": agent_ids})

    def unlink(self, agent_id: int) -> None:
        """
        Unlinks an agent.

        Args:
            agent_id (int): Id of the agent to unlink

        Example:

            >>> nessus.agents.unlink(agent_id)
        """
        self._delete(f"{agent_id}/unlink")

    def unlink_bulk(self, agent_ids: list[int]) -> None:
        """
        Unlinks multiple agents.

        Args:
            agent_ids (list[int]): List of agent ids to unlink

        Example:

            >>> nessus.agents.unlink_many([agent1, agent2, agent3])
        """
        self._delete("unlink", json={"ids": agent_ids})

    def details(self, agent_id: int) -> dict:
        """
        Returns the details for an agent.

        Args:
            agent_id (int): Id of the agent to retrieve

        Example:

            >>> agent = nessus.agents.details(agent_id)
        """
        return self._get(f"{agent_id}")["agents"][0]

    def list(
        self,
        limit: int = 1000,
        offset: int = 0,
        sort_by: str | None = None,
        sort_order: Literal["asc", "desc"] | None = None,
        search_type: Literal["and", "or"] | None = None,
        filters: dict | tuple | None = None,
        return_json: bool = False,
    ) -> PaginationIterator | list[dict]:
        """
        Returns a list of agents.

        Args:
            filters (list[tuple], optional):
                List of filters.
            sort_by (str, optional):
                Field to sort by
            sort_order (str, optional):
                Is the sort ascending (``asc``) or descending (``desc``)?
            limit (int, optional):
                Number of records per page
            offset (int, optional):
                How many records to skip before starting to return data
            return_json (bool, optional):
                Should a JSON object be returned instead of an iterator?

        Example:

            >>> for agent in nessus.agents.list():
            ...     print(agent)

            Example with filtering:

            >>> for agent in nessus.agents.list(
            ...     filters=[('name', 'match', 'lin')]
            ... ):
            ...     print(agent)

            Example getting the JSON response instead:

            >>> agents = nessus.agents.list(return_json=True)
        """
        schema = ListSchema()
        query = schema.dump(
            schema.load(
                {
                    "limit": limit,
                    "offset": offset,
                    "sort_by": sort_by,
                    "sort_order": sort_order,
                    "search_type": search_type,
                    "filters": filters,
                }
            )
        )
        if return_json:
            return self._get(params=query)["agents"]
        return PaginationIterator(
            self._api,
            limit=limit,
            offset=offset,
            query=query,
            envelope="agents",
            path=self._path,
        )
