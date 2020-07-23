# 2020-07-22 23:18:00 sky.cao

from typing import List
from collections import defaultdict


# 案例[1, 3, 2, 1,0,0]
class Solution1:
    def countTriplets(self, arr: List[int]) -> int:

        length, total = len(arr), 0
        dt = [0] * (length + 1)

        for i in range(1, length + 1):
            dt[i] = arr[i - 1] ^ dt[i - 1]

        for i in range(1, length):
            for j in range(i + 1, length + 1):
                if dt[j] ^ dt[i - 1] == 0:
                    total += j - i

        return total


# 案例[1, 3, 2, 1,0,0]
class Solution2:
    def countTriplets(self, arr) -> int:

        D = defaultdict(list)
        D[0], xor, ans = [-1], 0, 0  # D[0] 设为-1是为了配对，如果计算出一长串的异或值为0，如果不设置这个，将无法配对

        for i, a in enumerate(arr):
            xor ^= a
            D[xor].append(i)

        for A in D.values():
            # 将配对后的数据一一计算差值就是可以拆分的次数
            # D[1] = [0,3,4,5]  这个就说明，除了0号数等于1，后面1号到5号数的异或值为0
            # 那就是1-3为0，那么就是3-1
            # 1-4也是为0，那么就是4-1
            # 1-5也是为0，那么就是5-1
            # 4-4一个数， 4-4
            # 4-5为0， 5-4
            # 5-5一个数， 5-5
            for i in range(len(A) - 1):
                b = A[i] + 1
                for k in A[i + 1:]:
                    ans += k - b

        return ans


# 上一个算法的优化 案例[1, 3, 2, 1,0,0]
class Solution3:
    def countTriplets(self, arr) -> int:
        D = {0: (1, -1, 0)}  # 元祖记录（配对次数，最后配对的位置，这一次配对后可拆成几组）
        ans = xor = 0
        for i, a in enumerate(arr):
            xor ^= a
            if xor in D:
                n, last_k, sum = D[xor]
                sum += n * (i - last_k) - 1
                ans += sum
                D[xor] = (n + 1, i, sum)
            else:
                D[xor] = (1, i, 0)
        return ans


# i=0, D[1] = (1,0,0)
# i=1, D[2] = (1, 1, 0)}
# i=2, 匹配D[0]=(2, 2, 2) ans+=2
# i=3, 匹配D[1]=(2,3,2) ans+=2
# i=4, 匹配D[1]=(3,4,3) ans+=3
# i=5, 匹配D[1]=(4,5,5) ans+=5

# 为1是可以看出是一个递推公式