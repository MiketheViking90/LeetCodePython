from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sets = []
        set = []
        self.get_subsets(sets, set, nums, 0)
        return sets

    def get_subsets(self, sets, set, nums, idx):
        if idx == len(nums):
            to_add = list(set)
            sets.append(to_add)
            return

        self.get_subsets(sets, set, nums, idx+1)
        set.append(nums[idx])
        self.get_subsets(sets, set, nums, idx+1)
        set.pop()

nums = [1,2,3,4,5]
sets = Solution().subsets(nums)
print(sets)