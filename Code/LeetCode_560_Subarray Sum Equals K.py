class Solution(object):
    def subarraySum(self, nums, k):
        sumList = []
        total = 0
        count = 0

        for index, num in enumerate(nums):
            total += num
            want = total - k
            if want == 0:
                count += 1
                count += sumList.count(0)
            elif want != 0 and want in sumList:
                count += sumList.count(want)
            sumList.append(total)
        return count