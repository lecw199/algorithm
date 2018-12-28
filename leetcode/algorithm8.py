# coding : utf-8

class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        min = -2147483648
        max = 2147483647

        if not s:
            return 0

        s = s.strip()
        words = s.split()

        num = 0
        if words:
            word = words[0]
            word = word.split(".")[0]

            if not word:
                return 0

            array = []

            symbol = ''
            if word[0] in "-+":
                symbol = word[0]
                word = word[1:]

            for i in word:
                if i.isdigit():
                    array.append(i)
                else:
                    break

            if not array:
                return 0

            if array[0] == 0:
                while array[0] != 0:
                    array.pop(0)

            new = ''.join(array)
            if symbol:
                new = symbol+new

            try:
                num = int(new)
            except ValueError:
                pass

            if num:
                if num < min:
                    num = min

                if num > max:
                    num = max
                return num

        return num


a = Solution()

print(a.myAtoi("  -0012a42"))