class Solution(object):
    def romanToInt(self, s):
        res = 0
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i in range(len(s)):
            if i < len(s) - 1 and roman_map[s[i]] < roman_map[s[i + 1]]:
                res -= roman_map[s[i]]
            else:
                res += roman_map[s[i]] 

        return res


k = Solution()
print(k.romanToInt("MCMXCIV"))