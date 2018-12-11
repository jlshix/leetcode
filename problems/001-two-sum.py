# https://leetcode-cn.com/problems/two-sum/

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in range(len(nums)):
            tmp = target - nums[i]
            if tmp in dic:
                return [dic[tmp], i]
            else:
                dic[nums[i]] = i
        return None
