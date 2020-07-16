# 2020-07-16 22:11:00 sky.cao


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        def get_tree_nums(n):
            if n < 2:
                return 1
            elif n == 2:
                return 2

            t = 0  # 注意递归的写法
            for i in range(0, (n + 1) // 2):
                j = n - 1 - i

                if i == j:
                    s = get_tree_nums(i) * get_tree_nums(j)
                else:
                    s = get_tree_nums(i) * get_tree_nums(j) * 2

                t += s

            return t

        return get_tree_nums(n)