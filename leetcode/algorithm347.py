# 2020-07-18 22:19:00 sky.cao

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ret = {}
        for i in nums:
            ret[i] = 0 if i not in ret else ret[i] + 1

        ret = sorted(ret.items(), key=lambda x: x[1], reverse=True)

        return [x[0] for x in ret[:k]]
