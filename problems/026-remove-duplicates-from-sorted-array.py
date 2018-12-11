# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        
        i, j = 0, 1
        while j < len(nums):
            while j<len(nums) and nums[i] == nums[j]:
                nums.pop(j)
            i += 1
            j += 1
        return len(nums)