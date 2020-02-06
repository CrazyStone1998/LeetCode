# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def addTwoNumbers(self, l1, l2):
        cur_1 = l1
        cur_2 = l2
        temp = 0
        cur = l1
        while cur_1 and cur_2:
            k = cur_1.val + cur_2.val + temp
            if k >= 10:
                cur_1.val = k - 10
                temp = 1
            else:
                cur_1.val = k
                temp = 0
            cur = cur_1
            cur_1 = cur_1.next
            cur_2 = cur_2.next
        if cur_2:
            cur.next = cur_2
            cur_1 = cur_2
        if cur_1:
            while cur_1:
                k = cur_1.val + temp
                if k >= 10:
                    cur_1.val = k - 10
                    temp = 1
                else:
                    cur_1.val = k
                    temp = 0
                    break
                cur = cur_1
                cur_1 = cur_1.next
        if temp:
            cur.next = ListNode(1)
        return l1
