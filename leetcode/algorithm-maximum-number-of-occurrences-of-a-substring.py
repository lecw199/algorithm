# 2020-07-21 22:05:00 sky.cao


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:

        mn, rec, length = 0, {}, len(s)

        d = {}
        for i in range(length - minSize + 1):

            # 避免重复计算hash
            if i == 0:
                for v in s[i:i + minSize]:
                    d[v] = d.get(v, 0) + 1
            else:
                d[s[i - 1]] -= 1
                if d[s[i - 1]] <= 0:
                    del d[s[i - 1]]
                d[s[i + minSize - 1]] = d.get(s[i + minSize - 1], 0) + 1

            if len(d) > maxLetters:
                continue

            rec[s[i:i + minSize]] = rec.get(s[i:i + minSize], 0) + 1
            if rec[s[i:i + minSize]] > mn:
                mn = rec[s[i:i + minSize]]

        return mn
