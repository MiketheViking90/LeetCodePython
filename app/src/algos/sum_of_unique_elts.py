from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        n_to_cnt = {}
        for n in nums:
            cnt = n_to_cnt.get(n, 0)
            cnt += 1
            n_to_cnt[n] = cnt

        return sum([n for n, cnt in n_to_cnt.items() if cnt == 1])
