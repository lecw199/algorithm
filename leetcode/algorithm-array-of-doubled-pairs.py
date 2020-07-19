# 2020-07-19 17:43:00 sky.cao

from typing import List


class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:

        B = [i for i in A if i < 0]
        C = [i for i in A if i > 0]

        self.dt, count = {}, 0
        for i in A:
            self.dt[i] = self.dt.get(i, 0) + 1

        if self.dt.get(0, 0) > 0:
            if self.dt[0] % 2 != 0:
                return False
            else:
                del self.dt[0]

        B.sort(reverse=True)
        C.sort()

        return self.checkDouble(B) and self.checkDouble(C)

    def checkDouble(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            if self.dt[nums[i]] > 0:
                double = 2 * nums[i]
                if double not in self.dt or self.dt[double] == 0:
                    return False
                min = self.dt[double] if self.dt[double] < self.dt[nums[i]] else self.dt[nums[i]]
                self.dt[double], self.dt[nums[i]] = self.dt[double] - min, self.dt[nums[i]] - min

        return True
