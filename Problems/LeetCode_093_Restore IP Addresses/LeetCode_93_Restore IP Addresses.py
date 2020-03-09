class Solution:
    def __init__(self):
        self.res = []

    def restoreIpAddresses(self, s: str) -> "List[str]":
        self.backTracking(s, ["", "", "", ""], 0, 0)
        return self.res

    def backTracking(self, s: str, tmp:"List[int]", s_idx: "int", tmp_idx: "int"):
        if s_idx == len(s) - 1 and tmp_idx == 3:
            seg = tmp[tmp_idx] + s[s_idx]
            tmp[tmp_idx] = seg
            if int(seg) < 256:
                if self.check(s, tmp):
                    ip = ".".join([i for i in tmp])
                    if ip not in self.res:
                        self.res.append(ip)
        elif s_idx < len(s) - 1 and tmp_idx < 4:
            if len(tmp[tmp_idx]) == 0:
                newTmp = tmp.copy()
                newTmp[tmp_idx] = s[s_idx]
                self.backTracking(s, newTmp, s_idx + 1, tmp_idx)
                self.backTracking(s, newTmp, s_idx + 1, tmp_idx + 1)
            else:
                seg = tmp[tmp_idx] + s[s_idx]
                if len(seg) <=3 and int(seg) < 256:
                    newTmp = tmp.copy()
                    newTmp[tmp_idx] = seg
                    self.backTracking(s, newTmp, s_idx + 1, tmp_idx)
                    self.backTracking(s, newTmp, s_idx + 1, tmp_idx + 1)

    def check(self, s: "str", ip:"List[str]"):
        intTmp = [int(i) for i in ip]
        joinIP = "".join(str(seg) for seg in intTmp)
        return joinIP == s


myClass = Solution()
res = myClass.restoreIpAddresses("25525511135")
print(res)
