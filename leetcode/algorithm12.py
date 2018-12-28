# coding:utf-8


class Solution:
    def __init__(self):
        self.dict = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }
        self.bases = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        self.result = ''

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        self.t = num
        for base in self.bases:
            self.decompression(base)

        return self.result

    def decompression(self, base):
        n = int(self.t/base)
        self.result += n*self.dict[base]
        self.t = self.t - n*base


a = Solution()
print (a.intToRoman(1994))