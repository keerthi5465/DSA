from collections import Counter
class Solution(object):
    def searchRange(self, nums, target):
        count = Counter(nums)
        temp = 0
        low = 0
        high = len(nums) - 1
        for i,j in count.items():
            if i == target:
                temp = j
                break
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                if temp > 1:
                    for i in range(len(nums)):
                        if nums[i] == target:
                            return [i, i + (temp - 1)]
                else:
                    return [mid,mid]
                
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        

        return count

k = Solution()
print(k.searchRange([2,2],2))