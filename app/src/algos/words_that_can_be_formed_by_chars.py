from collections import Counter
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        formed_words = []
        chars_counter = Counter(chars)

        for word in words:
            if self.is_subset(Counter(word), chars_counter):
                formed_words.append(word)
        return sum([len(word) for word in formed_words])

    def is_subset(self, word_counter, char_counter):
        for key in word_counter:
            if word_counter[key] > char_counter.get(key, 0):
                return False
        return True

words = ["cat","bt","hat","tree"]
chars = "atach"

lens = Solution().countCharacters(words, chars)
print(lens)