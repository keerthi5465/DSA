class Solution(object):
    def search(self, nums, target):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return True
            if nums[low] < nums[mid]:
                if nums[low] < target < nums[mid]:
                    high = mid 
                else:
                    low = mid 
            else:
                if nums[high] > target > nums[mid]:
                    low = mid 
                else:
                    high = mid 
        return False

        

k = Solution()
print(k.search([1],1))