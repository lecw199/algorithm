# coding : utf-8

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if not s:
            return s

        length = len(s)

        if length == 1:
            return s
        elif length == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]

        max = 0
        x = None
        y = None

        dp = [[0 for _ in range(length)] for _ in range(length)]
        # init dp array
        for i in range(0, length-1):
            ed = i+3 if length > i+3 else length
            for j in range(i, ed):

                if i == j:
                    continue
                if s[i] == s[j]:
                    dp[i][j] = 1
                    if max < j-i+1:
                        max = j-i+1
                        x = i
                        y = j
                else:
                    dp[i][j] = 2

        for i in range(length-1, -1, -1):
            for j in range(i, length):
                print("i--> %s, j--> %s" % (i, j))
                if i == j or dp[i][j] > 0:
                    continue

                else:
                    if dp[i+1][j-1] == 1 and s[i] == s[j]:
                        dp[i][j] = 1
                        if max < j-i+1:
                            max = j-i+1
                            x = i
                            y = j

                    else:
                        dp[i][j] = 2

        print("x--> %s, y--> %s" % (x, y))
        if x is None or y is None:
            return s[0]
        return s[x:y+1]



a = Solution()

print(a.longestPalindrome("aaaa"))
