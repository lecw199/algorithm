# 2020-07-17 21:59:00 sky.cao

from typing import List


# 二分搜索要注意上界
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        length = len(nums)
        if target == nums[-1]:
            return length - 1
        elif target > nums[-1]:
            return length

        st, ed = 0, length - 1
        while True:
            md = (st + ed) // 2
            if nums[md] == target:
                return md
            elif nums[md] > target:
                if st == md:
                    return md
                ed = md
            elif nums[md] < target:
                if st == md:
                    return md + 1
                st = md
