from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for c in s:
            if self.is_open(c):
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if self.is_match(stack[-1], c):
                    stack.pop()
                else:
                    return False
        return len(stack) == 0

    def is_open(self, c):
        return c == '(' or c == '[' or c == '{'

    def is_match(self, left, right):
        if left == '(':
            return right == ')'
        elif left == '[':
            return right == ']'
        elif left == '{':
            return right == '}'
        return False


b = Solution().isValid('"(])"')
print(b)