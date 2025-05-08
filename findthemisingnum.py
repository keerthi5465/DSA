class Solution(object):
    def findKthPositive(self, arr, k):
        a = []
        maxk = max(arr) + k
        for i in range(1,maxk):
            if i not in arr:
                a.append(i)
        return a[k - 1]
        
            

k = Solution()
print(k.findKthPositive([1,2,3,4],2))