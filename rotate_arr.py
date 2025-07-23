class Solution(object):
    def rotate(self, nums, k):
        return k % len(nums)

        
        
p = Solution()
print(p.rotate([-1,-10,3,100],2))