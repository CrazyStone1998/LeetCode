# Definition for singly-linked list.
class ListNode:
    def __init__(self):
        self.val = None
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        l = len(lists)
        if not l:
            return None
        end = l - 1
        while end > 0:
            s = 0
            e = end
            while s < e:
                head = cur = ListNode()
                i, j = lists[s], lists[e]
                while i and j:
                    if i.val < j.val:
                        cur.next = i
                        i = i.next
                    else:
                        cur.next = j
                        j = j.next
                    cur = cur.next
                while i:
                    cur.next = i
                    i = i.next
                    cur = cur.next
                while j:
                    cur.next = j
                    j = j.next
                    cur = cur.next
                lists[s] = head.next
                s += 1
                e -= 1
            end //= 2
        return lists[0]
