from collections import Counter
from heapq import heappush, heappushpop
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_counts = Counter(words)
        heap = []

        for word, count in word_counts.items():
            heap_item = (count, word)
            if len(heap) < k:
                heappush(heap, heap_item)
            else:
                if count > heap[0][0]:
                    heappushpop(heap, heap_item)

        print(heap)
        freq = [word for (count, word) in heap]
        freq.reverse()
        return freq

words1 = ["i", "love", "leetcode", "i", "love", "coding"]
words2= ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4
freq = Solution().topKFrequent(words2, k)
print(freq)
