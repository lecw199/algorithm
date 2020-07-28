# 2020-07-24 22:44:00 sky.cao


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        p1 = tail = head
        p2 = head.next

        for i in range(n):
            if tail:
                tail = tail.next

        if not tail:
            return head.next

        while tail.next:
            p1 = p2
            p2 = p2.next
            tail = tail.next

        p1.next = p2.next

        return head
