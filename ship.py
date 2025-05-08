class Solution(object):
    def shipWithinDays(self, weights, days):
        low = max(weights)
        high = sum(weights)
        while low <= high:
            mid = (low + high) // 2
            cap = mid
            temp = 0
            day = 1
            for i in weights:
                if temp + i <= cap:
                    temp += i
                else:
                    temp = i
                    day += 1
            if day > days:
                low = mid + 1
            else:
                high =  mid - 1
        return low

k = Solution()
print(k.shipWithinDays([3,2,2,4,1,4],3))