# coding : utf-8
# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        def traver(L1, L2, offset=0):
            if L1 and L2:
                _sum = L1.val + L2.val + offset

                if offset:
                    offset = 0

                if _sum >= 10:
                    offset = 1
                    _sum -= 10
                tmp = ListNode(_sum)
                tmp.next = traver(L1.next, L2.next, offset)
                return tmp

            elif L1 and not L2:
                _sum = L1.val + offset

                if offset:
                    offset = 0

                if _sum >= 10:
                    offset = 1
                    _sum -= 10

                tmp = ListNode(_sum)
                tmp.next = traver(L1.next, L2, offset)
                return tmp

            elif not L1 and L2:
                _sum = L2.val + offset
                if offset:
                    offset = 0

                if _sum >= 10:
                    offset = 1
                    _sum -= 10

                tmp = ListNode(_sum)
                tmp.next = traver(L1, L2.next, offset)
                return tmp

            elif not L1 and not L2:
                if offset > 0:
                    tmp = ListNode(offset)
                    tmp.next = None
                    offset = 0
                    return tmp

        return traver(l1, l2)




