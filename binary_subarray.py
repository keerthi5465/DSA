class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        count = 0
        from collections import defaultdict

        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1  # one way to have sum 0 before we start

        count = 0
        current_sum = 0




        for num in nums:
            current_sum += num
            count += prefix_sums[current_sum - goal]
            prefix_sums[current_sum] += 1

        return count

k = Solution()
print(k.numSubarraysWithSum([1,0,1,0,1], 2))