# 2020-07-19 13:17:00 sky.cao

from typing import List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:

        ret = {}
        for i in answers:
            ret[i] = ret.get(i, 0) + 1

        total = 0
        for i in ret:
            if ret[i] > 1:
                d = ret[i] // (i + 1)
                if ret[i] % (i + 1) > 0:
                    d += 1

                total += d * (i + 1)
            else:
                total += i + 1

        return total