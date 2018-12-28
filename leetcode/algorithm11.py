# coding: utf-8

class Solution:
    def maxArea(self, s):
        """ idea： remove data from list, result is accurate, why?
        :type height: List[int]
        :rtype: int
        """
        length = len(s)
        self.s =s
        self.max = 0
        self.track(0, length-1)
        return self.max

    def f_min(self, x, y):
        return x if x < y else y

    def f_max(self, x, y):
        return x if x > y else y

    def track(self, st, ed):
        if st >= ed:
            return 0

        x = ed - st
        y = self.f_min(self.s[st], self.s[ed])
        area = x * y

        self.max = self.f_max(area, self.max)

        if self.s[st] >= self.s[ed]:
            next = self.track(st, ed-1)
        else:
            next = self.track(st+1, ed)

        return self.f_max(next, self.max)


a = Solution()

print(a.maxArea([1,8,6,2,5,4,8,3,7]))