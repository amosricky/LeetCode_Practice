# 【LeetCode】 933. Number of Recent Calls

## Description
Write a class RecentCounter to count recent requests.

It has only one method: ping(int t), where t represents some time in milliseconds.

Return the number of pings that have been made from 3000 milliseconds ago until now.

Any ping with time in [t - 3000, t] will count, including the current ping.

It is guaranteed that every call to ping uses a strictly larger value of t than before.

Note:

+ Each test case will have at most 10000 calls to ping.
+ Each test case will call ping with strictly increasing values of t.
+ Each call to ping will have 1 <= t <= 10^9.

## Example:

```
Input: inputs = ["RecentCounter","ping","ping","ping","ping"], inputs = [[],[1],[100],[3001],[3002]]
Output: [null,1,2,3,3]
```

## Solution1
* Use list to record it.

### Code1
```python
class RecentCounter:

    def __init__(self):
        self.time = []

    def ping(self, t: int) -> int:

        while len(self.time) > 0 and self.time[0] + 3000 < t:
            self.time.pop(0)
        self.time.append(t)
        return len(self.time)
```

###### tags: `LeetCode` `python` `Number of Recent Calls` 