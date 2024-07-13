"""
Plugin iterator module.
"""

from __future__ import annotations

from typing import Dict, List

from restfly.iterator import APIIterator


class PluginIterator(APIIterator):
    """
    PluginIterator class.
    """

    plugins: list[int] = []
    plugin_idx: int = 0
    total: int = None

    def __init__(self, api, **kw):
        super().__init__(api, **kw)
        for fam in self._api.plugins.families():
            family = self._api.plugins.family_details(fam["id"])
            self.plugins += [p["id"] for p in family["plugins"]]
        self.total = len(self.plugins)

    def __getitem__(self, idx: int) -> dict:
        return self._api.plugins.plugin_details(self.plugins[idx])

    def next(self):
        if self.plugin_idx >= self.total:
            raise StopIteration()
        self.plugin_idx += 1
        return self[self.plugin_idx - 1]
