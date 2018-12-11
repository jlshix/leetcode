# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        p, q = head, head.next
        while q:
            while q and p.val == q.val:
                p.next = q.next
                q = q.next
            p = p.next
            if q:
                q = q.next
        return head