class Solution(object):
    def minSubArrayLen(self, target, nums):
        l = 0
        min_v = float('inf')
        current_sum = 0
        for r in range(l,len(nums)):
            current_sum += nums[r]
            while current_sum >= target:
                min_v = min(min_v, r - l + 1)
                current_sum -= nums[l]
                l += 1
        return 0 if min_v == float('inf') else min_v


        
k = Solution()
print(k.minSubArrayLen(7,[2,3,1,2,4,3]))