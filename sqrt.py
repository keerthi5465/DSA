class Solution(object):
    def mySqrt(self, x):
        low = 1
        high = x
        while low <= high:
            mid = (low + high) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                return mid
                low = mid + 1
                
            else:
                high = mid 

k = Solution()
print(k.mySqrt(36))