# coding:utf-8

class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        dt = {}
        for i in A:
            if i not in dt:
                dt[i] = None
            else:
                return i


a = Solution()
print (a.repeatedNTimes([1,2,7,8,3,3,3,3]))