# https://leetcode-cn.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        try:
            return len(s.split()[-1])
        except:
            return 0