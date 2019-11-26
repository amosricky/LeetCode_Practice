class Solution:
    def __init__(self):
        self.res = []

    def deckRevealedIncreasing(self, deck: 'List[int]') -> 'List[int]':
        if not deck:
            return []

        target = sorted(deck)

        for index in range(len(deck) - 1, -1, -1):
            if len(self.res) < 2:
                self.res.insert(0, target[index])
            else:
                self.res = [target[index]] + [self.res[-1]] + self.res[:-1]

        return self.res


myClass = Solution()
result = myClass.deckRevealedIncreasing([17, 13, 11, 2, 3, 5, 7])
print(result)
