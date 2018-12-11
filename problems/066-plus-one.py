# https://leetcode-cn.com/problems/plus-one/

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = ''.join((str(x) for x in digits))
        return list(int(x) for x in (str(int(s) + 1)))
