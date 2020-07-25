# 【Codility】 Odds and evens problem

## Problem
![](https://i.imgur.com/TnZA4Ds.png)

### Code1
```python
def solution(A, K):
    # write your code in Python 3.6
    odds = [x for x in A if x % 2 == 1]
    odds = sorted(odds, reverse=True)
    evens = [x for x in A if x % 2 == 0]
    evens = sorted(evens, reverse=True)

    maxRes = 0
    for i in range(0, K+1):
        if i <= len(odds) and K-i <= len(evens):
            res = sum(odds[:i]) + sum(evens[:K-i])
            if res % 2 == 0:
                maxRes = max(maxRes, res)

    return maxRes
```

###### tags: `Codility` `python` 