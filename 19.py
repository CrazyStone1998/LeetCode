# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n: int):
        root = ListNode(-1)
        root.next = head
        left = right = root
        while n:
            right = right.next
            n -= 1
        while right.next:
            right = right.next
            left = left.next
        left.next = left.next.next
        return root.next





