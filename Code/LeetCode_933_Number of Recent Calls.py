class RecentCounter:

    def __init__(self):
        self.time = []

    def ping(self, t: int) -> int:

        while len(self.time) > 0 and self.time[0] + 3000 < t:
            self.time.pop(0)
        self.time.append(t)
        return len(self.time)

# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
param_1 = obj.ping(1)
param_2 = obj.ping(100)
param_3 = obj.ping(3001)
param_4 = obj.ping(3002)

print(param_1)
print(param_2)
print(param_3)
print(param_4)