class Solution:
    def numSubmatrixSumTarget(self, matrix: "List[List[int]]", target: "int") -> "int":
        m = len(matrix)
        n = len(matrix[0])
        count = 0
        for i in range(m):
            nums = [0] * n
            for j in range(i, m):
                for k in range(n):
                    nums[k] += matrix[j][k]
                count += self.subarraySum(nums, target)
        return count

    def subarraySum(self, nums: "List[int]", k: "int") -> "int":
        sumList = []
        total = 0
        count = 0

        for index, num in enumerate(nums):
            total += num
            want = total - k
            if want == 0:
                count += 1
                count += sumList.count(0)
            else:
                count += sumList.count(want)
            sumList.append(total)
        return count

myClass = Solution()
result = myClass.numSubmatrixSumTarget([[0, 1, 0], [1, 1, 1], [0, 1, 0]], 0)
print(result)