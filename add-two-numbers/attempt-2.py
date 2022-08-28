class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        head = ListNode(0)
        traverser = head
        rem = 0
        while (l1 != None or l2 != None or rem != 0):
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sum = x + y + rem
            rem = sum // 10
            new_node = ListNode(sum % 10)
            traverser.next = new_node
            traverser = new_node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head.next
"""
Results:
    Runtime: 55 ms, faster than 91.39% of Python online submissions for Add Two Numbers.
    Memory Usage: 13.5 MB, less than 68.24% of Python online submissions for Add Two Numbers.
"""