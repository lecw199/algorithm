# coding : utf-8


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        self.result = set()

        if not nums:
            return nums
        length = len(nums)

        if length < 3:
            return []

        zero_cnt = 0
        for i in nums:
            if i == 0:
                zero_cnt += 1

        if zero_cnt >= 3:
            self.result.add((0, 0, 0))

        postive = [x for x in nums if x > 0]
        negative = [ x for x in nums if x < 0 ]

        postive.sort()
        negative.sort()

        if zero_cnt:
            for i in negative:
                if -i in postive:
                    self.result.add((i, 0, -i))

        if postive and negative:
            len_a = len(postive)
            len_b = len(negative)
            self.complex(postive, negative, len_a, len_b)
            self.complex(negative, postive, len_b, len_a)

        ret = [list(x) for x in self.result]

        return ret

    def complex(self, a, b, len_a, len_b):
        for i in range(len_a-1):
            for j in range(i+1, len_a):
                print("i-->%s, s[i]--> %s, j-->%s, s[j]-->%s" % (i, a[i], j, a[j]))
                v = a[i]+a[j]

                if self.divide(-v, 0, len_b-1, b):
                    print ("%s-%s-%s" %(a[i], a[j], -v))
                    self.result.add((a[i], a[j], -v))

    def divide(self, x, st, ed, lst):
        print ("%s ===> %s" %(x,lst) )

        if lst[st] == x or lst[ed] == x:
            return True
        elif lst[st] > x or lst[ed] < x:
            return False
        while st <= ed:

            mid = int((st+ed)/2)
            if lst[mid] == x:
                return True
            elif lst[mid] < x:
                st = mid + 1
            else:
                ed = mid - 1
        return False

a = Solution()
print (a.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))