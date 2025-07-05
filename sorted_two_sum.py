class Solution(object):
    def twoSum(self, numbers, target):
        l = 0
        r = len(numbers) - 1
        while l <= r:
            mid = (l + r)//2
            if numbers[mid] + numbers[l] == target and mid != l:
                return [l + 1, mid + 1]
            elif numbers[mid] + numbers[l] > target:
                l = mid + 1
            else:
                r = mid - 1

k = Solution()
print(k.twoSum([-1,0], -1))