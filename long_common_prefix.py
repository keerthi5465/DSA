class Solution(object):
    def longestCommonPrefix(self, strs):
        res = ''
        for i in range(len(strs[0])):
            temp = strs[0][i]
            for j in strs[1:]:
                if i >= len(j) or j[i] != temp:
                    return res
            res += temp
        return res
    
k = Solution()
print(k.longestCommonPrefix(["flower","flow","flight"]))