from collections import defaultdict
class Solution(object):
    def numberOfSubarrays(self, nums, k):
        odd = defaultdict(int)
        odd_num = 0
        odd[0] = 1
        count = 0
        for num in nums:
            if num % 2 != 0:
                odd_num += 1
            count += odd[odd_num - k]
            odd[odd_num] += 1
        return count
    
k = Solution()
print(k.numberOfSubarrays([1,1,2,1,1],3))