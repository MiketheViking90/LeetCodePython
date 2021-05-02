from collections import Counter
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter_to_anagrams = {}
        for str in strs:
            str_counter = Counter(str)
            key = tuple(sorted(str_counter.items()))

            anagrams = counter_to_anagrams.get(key, [])
            anagrams.append(str)
            counter_to_anagrams[key] = anagrams
        return [anagram for anagram in counter_to_anagrams.values()]

strs = ["eat","tea","tan","ate","nat","bat"]
grams = Solution().groupAnagrams(strs)
print(grams)