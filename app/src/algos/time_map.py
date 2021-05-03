from collections import OrderedDict


class TimeMap:

    def __init__(self):
        self.history = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        key_history = self.history.get(key, OrderedDict())
        key_history[timestamp] = value
        self.history[key] = key_history

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.history.keys():
            return ''
        key_history: OrderedDict = self.history[key]
        filtered = [val for key, val in key_history.items() if timestamp <= key]
        if not filtered:
            return ''
        return filtered[0]

tm = TimeMap()
tm.set('k1', 'v1', 1)
v = tm.get('k1', 1)
print(v)

v = tm.get('k1', 3)
print(v)
tm.set('k1', 'v2', 3)
tm.set('k1', 'v3', 4)
