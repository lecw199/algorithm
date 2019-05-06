# coding : utf-8


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if not nums:
            return nums
        length = len(nums)
        result = []

        if length < 3:
            return []

        nums.sort()

        for t in range(length-1, 1, -1):
            if t < length-1 and nums[t+1] == nums[t]:
                continue

            v = -nums[t]
            i = 0
            j = t-1
            print ("---%s" % v)
            while i < j:
                sm = nums[i] + nums[j]
                if sm == v:
                    result.append([nums[i], nums[j], nums[t]])
                    while i < j and i < length-2 and nums[i] == nums[i+1]:
                        i += 1
                    while i < j and j > 1 and nums[j] == nums[j-1]:
                        j -= 1

                    i += 1
                    j -= 1

                elif sm > v:
                    j -= 1

                elif sm < v:
                    i += 1

        return result


a = Solution()
print (a.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))