from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        l_prods = [0]*n
        r_prods = [0]*n

        prod = 1
        for i in range(0, n):
            prod *= nums[i]
            l_prods[i] = prod

        prod = 1
        for i in range(n-1, -1, -1):
            prod *= nums[i]
            r_prods[i] = prod

        prods = [0] * n
        for i in range(n):
            prods[i] = l_prods[i] * r_prods[i]
        return prods

nums = [1,2,3,4]
prods = Solution().productExceptSelf(nums)
print(prods)