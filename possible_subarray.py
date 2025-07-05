class Solution(object):
    def subarraySum(self, nums, k):
        curr = 0
        count = 0
        d = dict()
        d[0] = 1


        for r in range(len(nums)):
            curr += nums[r]
            if curr - k in d:
                count += d[curr - k]
            d[curr] = d.get(curr,0) + 1
        return count

k = Solution()
print(k.subarraySum([1,2,3],3))