# coding: utf-8


class Solution:
    def maxArea(self, s):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(s)
        dp = [[0 for _ in range(length)] for _ in range(length)]

        f_max = lambda x, y: x if x > y else y
        f_min = lambda x, y: x if x < y else y


        for i in range(length - 1):
            t = f_min(i + 2, length)
            for j in range(i + 1, t):
                value = (j-i)*f_min(s[i], s[j])
                dp[i][j] = (j - i) * value

        for i in range(length - 1, -1, -1):
            for j in range(i, length):
                if i == j or dp[i][j]:
                    continue
                else:
                    dp[i][j] = f_max(f_max(dp[i + 1][j], dp[i][j - 1]), (j-i)*f_min(s[i], s[j]))

        return dp[0][length-1]


a = Solution()

print(a.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
