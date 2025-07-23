class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        r = len(nums) - k 
        arr = nums[0:r]
        nums[0:r] = []
        nums.extend(arr)
        return nums
    
k = Solution()
print(k.rotate([-1,-100,3,99],2))
