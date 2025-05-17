class Solution(object):
    def romanToInt(self, s):
        res = 0
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i in range(len(s)):
            if s[i] == 'V' and s[i - 1] == 'I':
                res += 4
            elif s[i] == 'X' and s[i - 1] == 'I':
                res += 9
            elif s[i] == 'L' and s[i - 1] == 'X':
                res += 40
            elif s[i] == 'C' and s[i - 1] == 'X':
                res += 90
            elif s[i] == 'D' and s[i - 1] == 'C':
                res += 400
            elif s[i - 1] == 'C' and s[i] == 'M' :
                res += 900
            else:
                res += roman_map[s[i]] 

        return res

k = Solution()
print(k.romanToInt("MCMXCIV"))