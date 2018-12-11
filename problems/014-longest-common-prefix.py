# https://leetcode-cn.com/problems/longest-common-prefix

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        s = strs[0]
        e = 1
        while all((x.find(s[:e]) == 0 for x in strs)) and e <= len(s):
            e += 1
        return s[:e-1]
