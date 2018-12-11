# https://leetcode-cn.com/problems/excel-sheet-column-number/

class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = '*ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        nums = list(s)
        res = 0
        level = 0
        while nums:
            letter = nums.pop()
            res += letters.find(letter) * 26 ** level
            level += 1
        return res