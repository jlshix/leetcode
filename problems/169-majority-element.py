# https://leetcode-cn.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for n in nums:
            if n in dic:
                dic[n] += 1
            else:
                dic[n] = 1
        rev = dict([v, k] for k, v in dic.items())
        return rev[max(rev.keys())]