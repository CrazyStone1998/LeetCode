# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeZeroSumSublists(self, head):
        d = {}
        total = 0
        root = ListNode(0)
        root.next = head
        head = root
        while head:
            total += head.val
            d[total] = head
            head = head.next
        total = 0
        head = root
        while head:
            total += head.val
            head.next = d.get(total).next
            head = head.next
        return root.next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(-3)
# head.next.next.next.next = ListNode(-2)
head = Solution().removeZeroSumSublists(head)
while head:
    print(head.val)
    head= head.next


