class Solution:
    def merge(self, nums1: 'List[int]', m: 'int', nums2: 'List[int]', n: 'int') -> 'None':
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        if m == 0:
            nums1[:n+1] = nums2
            return

        index1 = m - 1
        index2 = n - 1

        while index1 > -1 and index2 > -1:
            if nums1[index1] <= nums2[index2]:
                nums1[index1 + index2 + 1] = nums2[index2]
                index2 -= 1
            else:
                nums1[index1 + index2 + 1] = nums1[index1]
                index1 -= 1

        if index2 > -1:
            nums1[:index2 + 1] = nums2[:index2 + 1]


myClass = Solution()
myClass.merge([2, 0], 1, [1], 1)
