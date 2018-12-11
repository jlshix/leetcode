# https://leetcode-cn.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low, high = 0, x
        while low <= high:
            mid = (low + high) // 2
            if mid ** 2 == x:
                return mid
            elif mid ** 2 < x:
                low = mid + 1
            else:
                high = mid - 1
        return high