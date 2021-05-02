from collections import Counter
from heapq import heappush, heappop


class Solution:
    def frequencySort(self, s: str) -> str:
        s_counter = Counter(s)
        pq = []
        for char, count in s_counter.items():
            heap_item = (-count, char)
            heappush(pq, heap_item)
        s = ''
        while pq:
            count, char = heappop(pq)
            s += (char * -count)
        return s

s = Solution().frequencySort('tree')
print(s)
