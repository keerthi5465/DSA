class Solution(object):
    def numberOfSubarrays(self, nums, k):
        count = 0
        left = 0

        for right in range(len(nums)):

            if nums[right] % 2 != 0:
                k -= 1
                if k == 0:
                    count += 1
                    left += 1
                    k = k
        return count

k = Solution()
print(k.numberOfSubarrays([1,1,2,1,1], 3))