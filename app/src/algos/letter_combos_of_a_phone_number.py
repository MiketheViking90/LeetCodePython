from typing import List

digits_to_numbers = {
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z'],
}
class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        combos = []
        if not digits:
            return combos
        self.get_combos_recur(combos, '', digits, 0)
        return combos

    def get_combos_recur(self, combos, combo, digits, idx):
        if (idx == len(digits)):
            combos.append(combo)
            return

        digit = int(digits[idx])
        numbers: List[int] = digits_to_numbers.get(digit, [])
        for number in numbers:
            self.get_combos_recur(combos, combo + number, digits, idx+1)



sol = Solution()
digits = '423456'
combos = sol.letterCombinations(digits)
print(combos)