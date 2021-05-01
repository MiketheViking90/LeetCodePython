from builtins import str
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return True

        found_break = False
        for word in wordDict:
            if s.startswith(word):
                found_break |= self.wordBreak(s[len(word):len(s)], wordDict)
                if found_break:
                    return True
        return found_break

s = 'cars'
dict = ['car', 'ca', 'rs']
b = Solution().wordBreak(s, dict)
print(b)
