# 【LeetCode】 950. Reveal Cards In Increasing Order

## Description
In a deck of cards, every card has a unique integer.  You can order the deck in any order you want.

Initially, all the cards start face down (unrevealed) in one deck.

Now, you do the following steps repeatedly, until all cards are revealed:

1. Take the top card of the deck, reveal it, and take it out of the deck.
2. If there are still cards in the deck, put the next top card of the deck at the bottom of the deck.
3. If there are still unrevealed cards, go back to step 1.  Otherwise, stop.

Return an ordering of the deck that would reveal the cards in increasing order.

The first entry in the answer is considered to be the top of the deck.

Note:

+ 1 <= A.length <= 1000
+ 1 <= A[i] <= 10^6
+ A[i] != A[j] for all i != j

## Example:

```
Input: [17,13,11,2,3,5,7]
Output: [2,13,3,11,5,17,7]
Explanation: 
We get the deck in the order [17,13,11,2,3,5,7] (this order doesn't matter), and reorder it.
After reordering, the deck starts as [2,13,3,11,5,17,7], where 2 is the top of the deck.
We reveal 2, and move 13 to the bottom.  The deck is now [3,11,5,17,7,13].
We reveal 3, and move 11 to the bottom.  The deck is now [5,17,7,13,11].
We reveal 5, and move 17 to the bottom.  The deck is now [7,13,11,17].
We reveal 7, and move 13 to the bottom.  The deck is now [11,17,13].
We reveal 11, and move 17 to the bottom.  The deck is now [13,17].
We reveal 13, and move 17 to the bottom.  The deck is now [17].
We reveal 17.
Since all the cards revealed are in increasing order, the answer is correct.
```

## Solution1
* 先排序後逆推回去。
* 由最大的數開始 insert 入 res。
* 從第三個開始，insert 前須把 res 最後一個值拉來第一個再 insert 新數值。

### Code1
```python
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
```
## Solution2
* 邏輯一樣 ， 但用 deque。

### Code2
```python
from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: 'List[int]') -> 'List[int]':
        res = deque()
        deck.sort()
        for card in deck:
            res.rotate()
            res.appendleft(card)

        return list(res)
```

###### tags: `LeetCode` `python` `Reveal Cards In Increasing Order` 