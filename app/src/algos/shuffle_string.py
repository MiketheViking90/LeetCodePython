from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(s)
        ordered = [''] * n
        for i in range(n):
            c = s[i]
            j = indices[i]
            ordered[j] = c
        return ''.join(ordered)

s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
s1 = Solution().restoreString(s, indices)
print(s1)