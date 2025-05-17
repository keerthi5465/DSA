class Solution(object):
    def maxDepth(self, s):
        k = 0
        res = 0
        for i in s:
            if i == '(':
                k += 1
                res = max(k,res)
            elif i == ')':
                k -= 1
        return res


        
k = Solution()
print(k.maxDepth("(1+(2*3)+((8)/4))+1"))