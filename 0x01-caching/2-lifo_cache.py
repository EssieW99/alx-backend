#!/usr/bin/env python3
""" LIFO Caching """

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO class caching system """

    def __init__(self):
        """ initialization of the FIFOCache class"""

        super().__init__()

    def put(self, key, item):
        """ assigns to the dictionary the item for the key """

        if key is None or item is None:
            return

        if key in self.cache_data.keys():
            value = self.cache_data.pop(key)
            self.cache_data[key] = value
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_item = list(self.cache_data.keys())[-2]
            del self.cache_data[last_item]
            print(f'DISCARD: {last_item}')

    def get(self, key):
        """ returns the value linked to the key in the dict """

        if key is None or key not in self.cache_data:
            return None

        return self.cache_data.get(key)
