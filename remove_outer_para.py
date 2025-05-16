from collections import Counter
class Solution(object):
    def removeOuterParentheses(self, s):
        ans = ''
        k = 0
        for i in s:
            
            if k == 0 and i == '(':
                ans += i
                k = 1
            elif i == '(':
                if k == -1:
                    ans += i
                k = 1
            elif i == ')':
                if k == 1:
                    ans += i
                k = -1
        return ans
        

k = Solution()
print(k.removeOuterParentheses("(()())(())(()(()))"))