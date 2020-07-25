# 【Codility】 Min number of gamble rounds

## Problem
![](https://i.imgur.com/GfzkIR5.png)
![](https://i.imgur.com/OprjjFH.png)

## Solution
* That's a easy dynamic problem. Maybe could enhance the algo and get a better solution.
* Something like:
if K == 0, return N-1 directly.

### Code1
```python
def solution(N, K):
    # write your code in Python 3.6
    rounds = 0
    betAll = K

    chips = N

    while chips > 1:
        if chips % 2 == 0 and betAll > 0:
            chips = chips//2
            betAll -= 1
        else:
            chips -= 1
        rounds += 1

    return rounds
```

###### tags: `Codility` `python` 