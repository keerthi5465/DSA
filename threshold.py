import math
class Solution(object):
    def smallestDivisor(self, nums, threshold):
        low = 1
        high = max(nums)
        ans = 0
        while low <= high:
            rem = 0
            mid = (low + high) // 2
            for i in nums:
                rem +=  math.ceil(i / float(mid))
            
            if rem <= threshold:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans



        
        
    
k=Solution()
print(k.smallestDivisor([1,2,5,9], 6))