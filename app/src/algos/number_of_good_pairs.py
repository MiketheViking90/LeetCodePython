from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n = len(nums)
        good_pairs = []
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    good_pairs.append([i, j])
        return len(good_pairs)
