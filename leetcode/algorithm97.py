# 2020-07-19 10:45:00 sky.cao


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        s1_len = len(s1) + 1
        s2_len = len(s2) + 1

        if s1_len + s2_len - 2 != len(s3):
            return False

        dp = [[False for j in range(s1_len)] for i in range(s2_len)]
        dp[0][0] = True
        for i in range(1, s2_len):
            if dp[i - 1][0]:
                if s2[i - 1] == s3[i - 1]:
                    dp[i][0] = True
            else:
                break

        for j in range(1, s1_len):
            if dp[0][j - 1]:
                if s1[j - 1] == s3[j - 1]:
                    dp[0][j] = True
            else:
                break

        for i in range(1, s2_len):
            for j in range(1, s1_len):

                if s3[i + j - 1] == s2[i - 1] and dp[i - 1][j]:
                    dp[i][j] = True

                if s3[i + j - 1] == s1[j - 1] and dp[i][j - 1]:
                    dp[i][j] = True

        return dp[s2_len - 1][s1_len - 1]
