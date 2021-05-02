from collections import Counter
from heapq import heappush, heappushpop
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_counts = Counter(words)
        heap = []

        for word, count in word_counts.items():
            heap_item = (-count, word)
            if len(heap) < k:
                heappush(heap, heap_item)
            else:
                heappushpop(heap, heap_item)

        return [word for (count, word) in heap]

words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4
freq = Solution().topKFrequent(words, k)
print(freq)
