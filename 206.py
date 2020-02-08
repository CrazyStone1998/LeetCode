# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):

    # 迭代
        if head is None:
            return head
        child = head.next
        head.next = None
        while head and child:
            temp = child.next
            child.next = head
            head = child
            child = temp
        return head


head = ListNode(3)
head.next = ListNode(5)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(-2)
Solution().reverseList(head)
