class Solution(object):
    def lengthOfLIS(self, nums):
        dp = [1] * len(nums)  # dp[i] = LIS ending at index i

        for i in range(1, len(nums)):
            print(nums)
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return dp


k = Solution()
print(k.lengthOfLIS([4,10,4,3,8,9]))