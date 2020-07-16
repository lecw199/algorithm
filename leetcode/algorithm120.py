# 2020-07-16 22:07:00 sky.cao


class Solution(object):

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        length = len(triangle)

        if length == 0:
            return 0

        for i in range(length - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += triangle[i + 1][j] if triangle[i + 1][j] < triangle[i + 1][j + 1] else triangle[i + 1][j + 1]

        return triangle[0][0]
