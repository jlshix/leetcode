# https://leetcode-cn.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        l3 = ListNode(0)
        tmp = l3
        
        while l1 or l2:
            if l1 is None:
                l3.next = l2
                break
            if l2 is None:
                l3.next = l1
                break
            
            if l1.val < l2.val:
                node = ListNode(l1.val)
                l3.next = node
                l3 = node
                l1 = l1.next
            elif l1.val > l2.val:
                node = ListNode(l2.val)
                l3.next = node
                l3 = node
                l2 = l2.next
            else:
                node1 = ListNode(l1.val)
                node2 = ListNode(l2.val)
                l3.next = node1
                node1.next = node2
                l3 = node2
                l1 = l1.next
                l2 = l2.next
        return tmp.next