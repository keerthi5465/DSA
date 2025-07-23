class Solution(object):
    def sortColors(self, nums):
        for i in range(0,len(nums)):
            if nums[i] <= nums[i - 1]:
                nums[i],nums[i-1] = nums[i - 1],nums[i]
        return nums
    

k = Solution()
print(k.sortColors([2,0,2,1,1,0]))