class Solution:
    def arrangeWords(self, text: str) -> str:
        words = text.split(' ')
        ordered = [word.lower() for word in sorted(words, key=lambda word : len(word))]
        lower = ' '.join(ordered)
        return lower[0].upper() + lower[1: len(lower)]

text = "Keep calm and code on"
sent = Solution().arrangeWords(text)
print(sent)
