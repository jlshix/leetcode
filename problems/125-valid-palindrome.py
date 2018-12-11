# https://leetcode-cn.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '':
            return True
        s = self.beautify(s)
        
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True
    
    def beautify(self, s):
        s = s.upper()
        res = []
        for c in s:
            serial = ord(c)
            if serial in range(48, 58) or serial in range(65, 91):
                res.append(c)
        return ''.join(res)

# TODO 160ms ver ↑