from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        s_c = Counter(s)
        t_c = Counter(t)
        m= 0
        for i,j in s_c.items():
            for k,p in t_c.items():
                if i == k and j == p:
                    m += p
        return True if m == len(s) else False
    
k = Solution()
print(k.isAnagram('anna','nnaa'))