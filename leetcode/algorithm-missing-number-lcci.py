# 2020-07-20 12:20:00 sky.cao

from typing import List


# 利用异或相同则消失的原理
class Solution1:
    def missingNumber(self, nums: List[int]) -> int:
        ret = len(nums)
        for i in range(len(nums)):
            ret ^= i ^ nums[i]

        return ret


# 数学
class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        return len(nums) * (len(nums) + 1) // 2 - sum(nums)
