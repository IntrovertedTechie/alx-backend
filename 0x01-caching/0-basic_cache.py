#!/usr/bin/env python3
"""
Basic Cache
"""
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """ Basic cache system class"""

    def __init__(self) -> None:
        """
        Instantiates a Basic Cache
        """
        super().__init__()

    def put(self, key, item):
        """
        puts an item 
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
       return the value from storage            linked to `key`
        """
        return self.cache_data.get(key)
