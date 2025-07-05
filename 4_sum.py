class Solution(object):
    def fourSum(self, nums, target):
        res = []
        nums.sort()
        for i in range(len(nums)):
            for j in range(len(nums)- 1, -1 ,-1):
                l = i + 1
                r = j - 1
                while l < r:
                    sums = nums[i] + nums[j] + nums[l] + nums[r]

                    if sums < target:
                        l += 1
                    elif sums > target:
                        r -= 1
                    else:
                        lap = [nums[i],nums[j],nums[l],nums[r]]
                        if lap not in res:
                            res.append(lap)
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[ r - 1]:
                            r -= 1
                        l += 1
                        r -= 1
        return res

k = Solution()
print(k.fourSum([2,2,2,2,2],8))