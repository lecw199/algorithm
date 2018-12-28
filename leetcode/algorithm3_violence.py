# coding: utf-8

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        record = set()

        max = 0
        lens = len(s)
        for st in range(lens):
            if lens - st <= max:
                break
            for ed in range(st + 1 + max, lens+1):
                if ed-st <= max:
                    break

                for idx, i in enumerate(s[st:ed]):
                    if i not in record:
                        record.add(i)
                    else:
                        length = len(record)
                        if max < length:
                            max = length

                        record.clear()
                        record.add(i)

                        if ed > lens:
                            break
                if record:
                    length = len(record)

                    if max < length:
                        max = length

                    record.clear()
        return max


a = Solution()
print (a.lengthOfLongestSubstring("abcabcbb"))