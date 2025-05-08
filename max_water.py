
class Solution(object):
    def maxArea(self, height):
        max_water = 0
        for i in range(len(height)):
            for j in range(i,len(height)):
                dist = j - i
                min_val = min(height[i],height[j])
                max_water = max(max_water,dist * min_val)
        return max_water

m = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(m.maxArea(height))
