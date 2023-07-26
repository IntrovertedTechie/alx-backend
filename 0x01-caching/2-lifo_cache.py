#!/usr/bin/python3
"""Create Last In First Out Cache """
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ Define LIFOCache """

    def __init__(self):
        """ Initialize LIFOCache """
        self.stack = []
        super().__init__()

    def put(self, key, item):
        """Put"""
        if key and item:
            if self.cache_data.get(key):
                self.stack.remove(key)
            while len(self.stack) >= self.MAX_ITEMS:
                delete = self.stack.pop()
                self.cache_data.pop(delete)
                print('DISCARD: {}'.format(delete))
            self.stack.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Return key """
        return self.cache_data.get(key)
