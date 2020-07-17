# 2020-07-17 22:36:00 sky.cao

from typing import List


class Solution:
    def pairSums(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        i, j = 0, len(nums) - 1

        ret = []
        while i < j:
            sum = nums[i] + nums[j]
            if sum > target:
                j -= 1
            elif sum < target:
                i += 1
            else:
                ret.append((nums[i], nums[j]))
                i += 1
                j -= 1

        return ret
