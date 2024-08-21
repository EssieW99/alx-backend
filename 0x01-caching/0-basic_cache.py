#!/usr/bin/env python3
""" Basic dictionary """

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ a caching system """

    def __init__(self):
        """ initialization of the BasicCache class"""

        super().__init__()

    def put(self, key, item):
        """ assigns to the dictionary the item for the key """

        if key is None or item is None:
            return

        self.cache_data[key] = item

    def get(self, key):
        """ returns the value linked to the key in the dict """

        if key is None or key not in self.cache_data:
            return None

        return self.cache_data.get(key)
