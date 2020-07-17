# 2020-07-17 23:53:00 sky.cao

from typing import List


class Solution:
    direction = [(-1, 0), (0, 1), (0, -1), (1, 0)]

    def islandPerimeter(self, grid: List[List[int]]) -> int:

        dc = {(i, j): None for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j]}

        s = len(dc) * 4
        for u in dc:
            for i in self.direction:
                if (i[0] + u[0], i[1] + u[1]) in dc:
                    s -= 1

        return s