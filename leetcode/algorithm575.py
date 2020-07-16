# 2020-07-16 22:09:00 sky.cao

from typing import List


class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        systers = {i: None for i in candies}
        max = len(candies) // 2
        return len(systers) if len(systers) <= max else max
