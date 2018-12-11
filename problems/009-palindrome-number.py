# https://leetcode-cn.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == ''.join(reversed(str(x)))
