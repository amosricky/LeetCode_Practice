# Binary Search
class Solution:
    def mySqrt(self, x: 'int') -> 'int':
        if x == 1 or x == 0:
            return x

        left, right = 0, x
        while left <= right:
            mid = left + (right - left) // 2

            if mid * mid > x:
                right = mid - 1
            elif mid * mid < x:
                left = mid + 1
            else:
                return mid
        return right

# Newton’s Method
# class Solution:
#     def mySqrt(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
#
#         # approach: Newton's method for root-finding
#
#         result = x
#         while not result * result - x < 1:
#             result = (result + x / result) / 2
#
#         return int(result)


myClass = Solution()
result = myClass.mySqrt(13)
print(result)
