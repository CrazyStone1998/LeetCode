# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head, m: int, n: int):
        root = ListNode(0)
        root.next = head
        start = head = root
        pos = 0
        while pos < m:
            start = head
            head = head.next
            pos += 1
        child = head.next
        while pos < n:
            temp = child.next
            child.next = head
            head = child
            child = temp
            pos += 1
        start.next.next = child
        start.next = head
        return root.next
head = ListNode(3)
head.next = ListNode(5)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(-2)
head = Solution().reverseBetween(head,1,1)
while head:
    print(head.val)
    head= head.next
