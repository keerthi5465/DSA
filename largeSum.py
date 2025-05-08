class Solution(object):
    def splitArray(self, nums, k):
        low = max(nums)
        high = sum(nums)
        best = 0
        while low <= high:
            mid = (low + high) // 2
            l = 1
            lows = 0
            for i in nums:
                if lows + i > mid:
                    l += 1
                    lows = i
                else:
                    lows += i
            if l <= k:
                best = mid
                high = mid - 1
            else:
                low = mid + 1
        return best
                
k = Solution()
print(k.splitArray([1,2,3,4,5],2))