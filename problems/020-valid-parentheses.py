# https://leetcode-cn.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {')': '(', ']': '[', '}': '{'}
        stack = []
        for x in s:
            if x in '([{':
                stack.append(x)
            if x in ')]}':
                if stack == [] or not dic[x] == stack.pop():
                    return False
        return stack == []
