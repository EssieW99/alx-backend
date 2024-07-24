#!/usr/bin/python3
""" LIFOCache class """

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO Caching class """

    def __init__(self):
        """ initialization of the parent class """

        super().__init__()

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data the item value for the key key
        """

        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = list(self.cache_data.keys())[-2]
            del self.cache_data[last_key]
            print(f'DISCARD: {last_key}')

    def get(self, key):
        """
        return the value in self.cache_data linked to key
        """

        if key is None:
            return None

        return self.cache_data.get(key, None)
