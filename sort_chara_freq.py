from collections import Counter
class Solution(object):
    def frequencySort(self, s):
        s_c = Counter(s)
        sorted_s = sorted(s_c.items(), key = lambda x: -x[1])
        return ''.join(char * count for char, count in sorted_s)
    
p=Solution()
print(p.frequencySort('keerthk'))