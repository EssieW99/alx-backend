#!/usr/bin/env python3
""" LFU Caching """

from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LFU class caching system """

    def __init__(self):
        """ initialization of the LFUCache class"""

        super().__init__()
        self.cache_data = OrderedDict()
        self.usage_frequency = {}

    def put(self, key, item):
        """ assigns to the dictionary the item for the key """

        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.usage_frequency[key] += 1
            self.cache_data.move_to_end(key)

        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                least_freq = min(self.usage_frequency.values())
                lfu_keys = [k for k, v in self.usage_frequency.items()
                            if v == least_freq]
                if len(lfu_keys) > 1:
                    lfu_key = next(iter(self.cache_data))
                    for k in lfu_keys:
                        if k in self.cache_data:
                            lfu_key = k
                            break
                else:
                    lfu_key = lfu_keys[0]

                del self.cache_data[lfu_key]
                del self.usage_frequency[lfu_key]
                print(f'DISCARD: {lfu_key}')

        self.cache_data[key] = item
        self.usage_frequency[key] = 1

    def get(self, key):
        """ returns the value linked to the key in the dict """

        if key is None or key not in self.cache_data:
            return None

        self.usage_frequency[key] += 1
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
