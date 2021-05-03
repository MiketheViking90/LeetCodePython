class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set = set(jewels)
        return len({stone for stone in list(stones) if stone in jewels_set})


print(set('aAbbbB'))