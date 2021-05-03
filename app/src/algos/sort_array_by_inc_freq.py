from collections import Counter
from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums_counter = Counter(nums)
        return sorted(nums, key=lambda x : (nums_counter[x], -x))
