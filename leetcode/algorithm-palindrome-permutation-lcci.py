# 2020-07-19 21:33:00 sky.cao

# elegant
class Solution1:
    def canPermutePalindrome(self, s: str) -> bool:
        dt = {}

        for i in s:
            dt[i] = dt.get(i, 0) + 1

        return sum([i % 2 for i in dt.values()]) <= 1


class Solution2:
    def canPermutePalindrome(self, s: str) -> bool:

        dt, count = {}, 0

        for i in s:
            dt[i] = dt.get(i, 0) + 1

        for i in dt:
            if dt[i] % 2 == 1:
                count += 1

        return count <= 1
