class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if not s or numRows < 2:
            return s

        length = len(s)
        line = ['' for _ in range(numRows)]

        single = numRows - 2

        idx = 0
        while idx < length + 1:
            for i, x in enumerate(s[idx: idx + numRows]):
                line[i] += x
            idx = idx + numRows

            for i, x in enumerate(s[idx: idx + single]):
                line[numRows - i - 2] += x
            idx = idx + single

        for i in line:
            print (i)

        return ''.join(line)


a = Solution()

print(a.convert("PAYPALISHIRING", 1))
