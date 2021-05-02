from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot_idx = self.binary_search_pivot(nums)
        if nums[pivot_idx] == target:
            return pivot_idx
        elif target < nums[len(nums) - 1]:
            return self.binary_search(nums, target, pivot_idx+1, len(nums)-1)
        else:
            return self.binary_search(nums, target, 0, pivot_idx-1)

    def binary_search_pivot(self, nums):
        lo = 0
        hi = len(nums)

        while lo <= hi:
            mid = (lo + hi) // 2

            n0 = nums[mid-1]
            n1 = nums[mid]
            if n0 >= n1:
                return mid
            elif (nums[lo] > n1):
                hi = mid-1
            else:
                lo = mid+1
        return -1

    def binary_search(self, nums, target, lo, hi):
        while lo <= hi:
            mid = (lo + hi) // 2
            n = nums[mid]
            if n == target:
                return mid
            elif target > n:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1


nums = [8,9,1,2,3,4,5,6,7]