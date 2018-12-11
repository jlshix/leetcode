# https://leetcode-cn.com/problems/add-binary/

class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        x = int(a, base=2) + int(b, base=2)
        return bin(x)[2:]