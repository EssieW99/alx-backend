#!/usr/bin/env python3
""" FIFO caching """

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO class caching system """

    def __init__(self):
        """ initialization of the FIFOCache class"""

        super().__init__()

    def put(self, key, item):
        """ assigns to the dictionary the item for the key """

        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_item = list(self.cache_data.keys())[0]
            del self.cache_data[first_item]
            print(f'DISCARD: {first_item}')

    def get(self, key):
        """ returns the value linked to the key in the dict """

        if key is None or key not in self.cache_data:
            return None

        return self.cache_data.get(key)
