#!/usr/bin/python3
""" BasicCache class """

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Caching System class """

    def __init__(self):
        """ initialization of the parent class """
        super().__init__()

    def put(self, key, item):
        """
        assigns a key its item value in the self.cache_data dictionary
        """

        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        return the value in self.cache_data linked to key
        """

        if key is None:
            return None

        return self.cache_data.get(key, None)
