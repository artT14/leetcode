# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#---------------------------------------------------------#
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # place = 1
        head = ListNode()
        traverser = head
        remainder = 0
                
        while (traverser):
            incr = traverser.val
            cond1 = l1 is not None
            cond2 = l2 is not None
            if cond1:
                incr += l1.val
                l1 = l1.next
            if cond2:
                incr += l2.val
                l2 = l2.next
            
            remainder = incr // 10
            incr = incr % 10
            
            traverser.val = incr
            traverser.next = ListNode(val=remainder) if cond1 or cond2 or remainder else None
            traverser = traverser.next
            
        return head

s = Solution()

a = ListNode(9)
b = ListNode(9,a)
c = ListNode(9,b)
d = ListNode(9,c)
e = ListNode(9,d)
f = ListNode(9,e)
g = ListNode(9,f)

a1 = ListNode(9)
b1 = ListNode(9,a1)
c1 = ListNode(9,b1)
d1 = ListNode(9,c1)

print(
    s.addTwoNumbers(g,f)
)

"""
RESULTS:
Wrong Answer
"""