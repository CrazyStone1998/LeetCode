# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        if not head:
            return head
        if not head.next:
            return head
        first = head
        second = head.next
        head = head.next
        parent = head
        while first and second:
            first.next = second.next
            parent.next = second
            second.next = first
            parent = first
            if not first.next:
                break
            second = first.next.next
            first = first.next
        return head