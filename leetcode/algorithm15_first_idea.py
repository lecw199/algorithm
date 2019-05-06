# coding : utf-8


def divide(x, st, ed, lst):
    print ("%s ===> %s" % (x, lst))

    if lst[st] == x:
        return True
    elif lst[st] > x:
        return False

    if lst[ed] == x:
        return True
    elif lst[ed] < x:
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


class Solution:
    def __init__(self):
        self.result = set()
        self.cnt = {}

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if not nums:
            return nums
        length = len(nums)

        if length < 3:
            return []

        positive = []
        negative = []
        zero_cnt = 0

        for i in nums:
            if i == 0:
                zero_cnt += 1
            elif i > 0:
                positive.append(i)
            elif i < 0:
                negative.append(-1)

        if zero_cnt >= 3:
            self.result.add((0, 0, 0))

        positive.sort()
        negative.sort()

        if zero_cnt:
            for i in negative:
                if i in positive:
                    self.result.add((i, 0, -i))

        if positive and negative:
            len_a = len(positive)
            len_b = len(negative)
            self.complex(positive, negative, len_a, len_b)
            self.complex(negative, positive, len_b, len_a)

        ret = [list(x) for x in self.result]

        return ret

    def complex(self, a, b, len_a, len_b):
        for i in range(len_a-1):
            for j in range(i+1, len_a):
                v = a[i]+a[j]

                if divide(-v, 0, len_b-1, b):
                    print ("%s-%s-%s" % (a[i], a[j], v))
                    self.result.add((a[i], a[j], v))


a = Solution()
print (a.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))