#!/usr/bin/env python3
"""MRU Cache module
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRU Cache class
    """

    def __init__(self):
        """Initialize
        """
        super().__init__()
        self.access_order = []

    def put(self, key, item):
        """Add an item in the cache with MRU algorithm
        """
        if key is None or item is None:
            return

        # Check if the key is already in the cache
        if key in self.cache_data:
            self.access_order.remove(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            # If cache is full, remove the most r)
            mru_key = self.access_order.pop()
            del self.cache_data[mru_key]
            print("DISCARD:", mru_key)

        # Add the new key at the end of the access_order list
        self.access_order.append(key)
        # Update the cache with the new item
        self.cache_data[key] = item

    def get(self, key):
        """Get an item from the cache with MRU algorithm
        """
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed key to the end)
        self.access_order.remove(key)
        self.access_order.append(key)

        return self.cache_data[key]
