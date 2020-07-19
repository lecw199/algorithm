# 2020-07-19 17:23:00 sky.cao


class Solution:
    def firstUniqChar(self, s: str) -> str:

        length = len(s)
        result, min = {}, length

        for i, v in enumerate(s):
            result[v] = i if v not in result else length

        for i in result:
            min = result[i] if min > result[i] else min

        return " " if min == length else s[min]