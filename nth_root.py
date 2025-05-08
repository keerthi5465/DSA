class Solution:
    def nth(self,num,n):
        low = 1
        high = num
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if  mid ** n <= num:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans

k = Solution()
print(k.nth(5,2))