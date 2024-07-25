#!/usr/bin/python3
""" MRUCache class"""

from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ MRU Caching class """

    def __init__(self):
        """ initialization of the parent class """

        super().__init__()
        self.cache_data = OrderedDict()  # keep track of the insertion order
        self.frequency = {}  # keep track of the usage frequency

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data the item value for the key key
        and handle MRU caching
        """

        if key is None or item is None:
            return

        """
        Update the item, move the key to the end to maintain LRU order
        for items with the same frequency
        """
        if key in self.cache_data:
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)
            self.frequency[key] += 1
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                """
                Find the key with the least frequency and if there are ties,
                the least recently used
                """
                least_freq = min(self.frequency.values())
                lfu_keys = [k for k, v in self.frequency.items()
                            if v == least_freq]
                """
                Resolve ties by removing the least recently used item
                among the least frequently used
                """
                if len(lfu_keys) > 1:
                    lfu_key = next(iter(self.cache_data))
                    for k in lfu_keys:
                        if k in self.cache_data:
                            lfu_key = k
                            break
                else:
                    lfu_key = lfu_keys[0]

                """ Remove the LFU item"""
                del self.cache_data[lfu_key]
                del self.frequency[lfu_key]
                print(f'DISCARD: {lfu_key}')

            """" Add the new key and item"""
            self.cache_data[key] = item
            self.frequency[key] = 1

    def get(self, key):
        """
        return the value in self.cache_data linked to key
        """

        if key is None or key not in self.cache_data:
            return None
        else:
            self.frequency[key] += 1
            """
            Move the accessed key to the end to maintain LRU order
            for items with the same frequency
            """
            self.cache_data.move_to_end(key)
            return self.cache_data.get(key, None)
