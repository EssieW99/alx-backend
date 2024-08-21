#!/usr/bin/env python3
""" MRU Caching """

from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ MRU class caching system """

    def __init__(self):
        """ initialization of the MRUCache class"""

        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ assigns to the dictionary the item for the key """

        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            self.cache_data[key] = item

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_item = list(self.cache_data.keys())[-2]
            del self.cache_data[last_item]
            print(f'DISCARD: {last_item}')

    def get(self, key):
        """ returns the value linked to the key in the dict """

        if key is None or key not in self.cache_data:
            return None

        self.cache_data.move_to_end(key)
        return self.cache_data.get(key)
