# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def isPalindrome(self, head) -> bool:
        # slow and quick
        if head is None or head.next is None:
            return True
        cur = half = head
        while half.next and half.next.next:
            cur = cur.next
            half = half.next.next
        cur = cur.next
        half = cur.next if cur.next else None
        cur.next = None
        while cur and half:
            temp = half.next
            half.next = cur
            cur = half
            half = temp
        while cur:
            if cur.val != head.val:
                return False
            cur = cur.next
            head = head.next
        return True


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(1)
print(Solution().isPalindrome(head))
