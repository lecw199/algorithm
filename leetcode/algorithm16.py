# coding: utf-8

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()

        max = nums[-1] + target
        length = len(nums)

        if length == 3:
            return nums

        for i in range(length-2):
            left = i+1
            right = i+2
            t = target-nums[i]

            while left < right:
                sm = nums[left] + nums[right]

                diff = t-sm
                if diff < 0:
                    diff = -diff

                print ("i--->%s,left--->%s, right--->%s, diff--->%s, max--->%s" % (i, left, right, diff, max))

                if diff == max:
                    if diff != target:
                        max = diff
                    if right < length - 1:
                        right += 1
                    elif left < right:
                        left += 1

                elif diff < max:
                    if diff != target:
                        max = diff
                    if right < length - 1:
                        right += 1
                    elif left < right:
                        left += 1

                elif diff > max:
                    break

        return max

a = Solution()
print (a.threeSumClosest([-1, 2, 1, -4], 1))