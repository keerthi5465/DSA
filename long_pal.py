class Solution(object):
    def longestPalindrome(self, s):
        x = []
        y = []
        result = ''
        for i in s:
            x.append(i)
        y = x[::-1]
        k = 0 
        for i in range(len(x)):
            if x[i] == y[i]:
                result += x[i]
        
            
        return result if result else x[0]

p = Solution()
print(p.longestPalindrome('as'))