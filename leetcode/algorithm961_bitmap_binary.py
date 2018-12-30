# coding: utf-8


class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        bit = [0 for _ in range(10001)]
        mid = int(len(A) / 2)
        for i in A[0:mid + 2]:
            bit[i] += 1
            if bit[i] > 1:
                return i


a = Solution()
print (a.repeatedNTimes([1,2,7,8,3,3,3,3]))