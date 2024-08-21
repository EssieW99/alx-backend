#!/usr/bin/env python3
""" LRU Caching"""

from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRU class caching system """

    def __init__(self):
        """ initialization of the LRUCache class"""

        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ assigns to the dictionary the item for the key """

        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_item = list(self.cache_data.keys())[0]
            del self.cache_data[first_item]
            print(f'DISCARD: {first_item}')

    def get(self, key):
        """ returns the value linked to the key in the dict """

        if key is None or key not in self.cache_data:
            return None

        self.cache_data.move_to_end(key)
        return self.cache_data.get(key)
