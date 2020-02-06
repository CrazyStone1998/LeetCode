# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k: int):
        chain = [None, ]
        root = head
        flag = True
        for i in range(1, k + 1):
            if not head:
                return root
            chain.append(head)
            head = head.next
        for j in range(k, 0, -1):
            chain[j].next = chain[j - 1]
        root = chain[k]
        end = chain[1]
        while head:
            start = head
            for i in range(1, k + 1):
                if not head:
                    flag = False
                    break
                chain[i] = head
                head = head.next
            if not flag:
                end.next = start
                break
            for j in range(k, 0, -1):
                chain[j].next = chain[j - 1]
            end.next = chain[k]
            end = chain[1]
        return root
