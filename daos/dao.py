import pickle
from abc import ABC, abstractmethod

class DAO(ABC):
    def __init__(self, datasource=''):
        self._datasource = datasource
        self._cache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self._cache, open(self._datasource, 'wb'))

    def __load(self):
        self._cache = pickle.load(open(self._datasource, 'rb'))

    def add(self, key, obj):
        self._cache[key] = obj
        self.__dump()

    def get(self, key):
        try:
            return self._cache[key]
        except KeyError:
            pass

    def remove(self, key):
        try:
            self._cache.pop(key)
            self.__dump()
        except KeyError:
            pass

    def get_all(self):
        return self._cache.values()