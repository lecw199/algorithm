# 2020-07-28 19:57:00 sky.cao

from typing import List


class Solution1:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False

        middle = total // 2

        dt = {nums[0]: None}
        for i in range(1, len(nums)):
            d = [x for x in dt]
            for j in d:
                dt[j + nums[i]] = None
                if middle in dt:
                    return True

        return False


# 推导式 dp[i][j] = dp[i][j-1]  if i<num[i] else dp[i-nums[j]][j-1] or dp[i][j-1]
# dp[i][j]代表前j个数的和是不是能凑出和为i，可以就为true，否则为false
class Solution2:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)
        if total % 2 == 1:
            return False

        middle = total // 2

        dp = [[False] * (len(nums)) for i in range(middle + 1)]

        for j in range(len(nums)):
            dp[0][j] = True

        for j in range(1, len(nums)):
            for i in range(middle + 1):
                dp[i][j] = dp[i][j - 1] if i < nums[j] else dp[i - nums[j]][j - 1] or dp[i][j - 1]

        return any([i for i in dp[middle]])


# dp的空间优化
# 原理，就是将序列方向，这样前面计算的值不会被覆盖
#  [1,2,3,5,1]

# j = 0, dp = [True, True, False, False, False, False, False]
# j = 1, dp = [True, True, True, True, False, False, False]
# j = 2, dp = [True, True, True, True, True, True, True]
# j = 3, dp = [True, True, True, True, True, True, True]
# j = 4, dp = [True, True, True, True, True, True, True]

class Solution3:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)
        if total % 2 == 1:
            return False

        middle = total // 2 + 1

        dp = [False for i in range(middle)]
        dp[0] = True

        for j in range(len(nums)):
            for i in range(middle - 1, -1, -1):
                dp[i] = dp[i] if i < nums[j] else dp[i - nums[j]] or dp[i]

        return dp[-1]
