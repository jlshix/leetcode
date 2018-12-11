# https://leetcode-cn.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums == [] or nums[0] > target:
            return 0
        if nums[-1] < target:
            return len(nums)
        if nums[-1] == target:
            return len(nums) - 1
        
        for i in range(len(nums) - 1):
            if nums[i] == target:
                return i
            if nums[i] < target and nums[i+1] > target:
                return i+1