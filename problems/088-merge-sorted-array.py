# https://leetcode-cn.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        for _ in range(len(nums1) - m):
            nums1.pop()
        for _ in range(len(nums2) - n):
            nums2.pop()
        nums1.extend(nums2)
        nums1.sort()
        