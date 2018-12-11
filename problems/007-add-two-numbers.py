# https://leetcode-cn.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(0)
        z = l3
        x = l1
        y = l2
        h = 0
        while x != None or y != None:
            if x == None:
                x = ListNode(0)
            if y == None:
                y = ListNode(0)
            
            t = x.val + y.val + h
            if t > 9:
                z.val = t - 10
                h = 1
            else:
                z.val = t
                h = 0
            
            if x.next or y.next or h == 1:
                z.next = ListNode(0)
            if not x.next and not y.next and h==1:
                z.next = ListNode(1)
            x = x.next
            y = y.next
            z = z.next
        return l3
