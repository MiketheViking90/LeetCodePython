from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parentheses = []
        self.generate(parentheses, '(', n-1, n)
        return parentheses

    def generate(self, parentheses, cur, l_count, r_count):
        if not l_count and not r_count:
            parentheses.append(cur)
            return

        if l_count and l_count <= r_count:
            self.generate(parentheses, cur + '(', l_count-1, r_count)
        if r_count and r_count >= l_count:
            self.generate(parentheses, cur + ')', l_count, r_count-1)

parens = Solution().generateParenthesis(3)
print(parens)