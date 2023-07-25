#!/usr/bin/env python3
  """
  First In First Out module
  """
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """
     Caching system based on the first in     first out cache replacement policy
    """

    def put(self, key, item):
        """puts item in the cache
        """
        if key and item:
            # if key is new for cache storage
            if not self.cache_data.get(key):
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    first = list(self.cache_data.keys())[0]
                    print("DISCARD: {}".format(first))
                    del self.cache_data[first]

            self.cache_data[key] = item

    def get(self, key):
        """
        return the value from storage
        """
        return self.cache_data.get(key)
