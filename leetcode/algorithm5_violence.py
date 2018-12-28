# coding:utf-8


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


        max = 0
        for st in range(length-1):
            tmp = max
            for end in range(length, tmp, -1):
                print ("%s ---> %s" %(st,end))
                if end - st <= max:
                    continue
                if self.check_palindromic(s[st:end]):
                    t = end - st
                    if max < t:
                        max = t
                        string = s[st:end]
        return string

    def check_palindromic(self, s):
        length = len(s)
        for i in range(int(length/2)):
            if s[i] != s[length-i-1]:
                return False

        return True


a = Solution()

print (a.longestPalindrome("babad"))






