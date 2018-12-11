# https://leetcode-cn.com/problems/excel-sheet-column-title/

class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        letters = '*ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        num = []
        
        while n > 0:
            rem = n % 26
            n = n // 26
            if rem == 0:
                rem = 26
                n -= 1
            num.append(letters[rem])
        return ''.join(reversed(num))