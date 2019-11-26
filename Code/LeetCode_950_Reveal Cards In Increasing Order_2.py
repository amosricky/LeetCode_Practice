from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck: 'List[int]') -> 'List[int]':
        res = deque()
        deck.sort()
        for card in deck:
            res.rotate()
            res.appendleft(card)

        return list(res)


myClass = Solution()
result = myClass.deckRevealedIncreasing([17, 13, 11, 2, 3, 5, 7])
print(result)
