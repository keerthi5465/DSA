class Solution(object):
    def longestOnes(self, nums, k):
        left = 0
        max_ones = 0

        for right in range(len(nums)):
            if nums[right] != 1:
                k -= 1
            while k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
                
            max_ones = max(max_ones, right - left + 1)
        return max_ones
    
k = Solution()
print(k.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3))