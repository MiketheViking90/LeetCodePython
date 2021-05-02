from heapq import heappop, heappush
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        for num in nums:
            if len(pq) < k:
                heappush(pq, num)
            else:
                if num > pq[0]:
                    heappop(pq)
                    heappush(pq, num)
        return pq[0]

nums = [3,1,4,5,9,2,6]
n = Solution().findKthLargest(nums, 2)
print(n)