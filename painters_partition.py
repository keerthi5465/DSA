class Solution:
    def painter(self,arr,k):
        low = max(arr)
        high = sum(arr)
        best = 0
        while low <= high:
            mid = (low + high) // 2
            l = 1
            lows = 0
            for i in arr:
                if lows + i > mid:
                    l += 1
                    lows = i
                else:
                    lows += i
            if l <= k:
                best = mid
                high = mid - 1
            else:
                low = mid + 1
        return best
    

k = Solution()
print(k.painter([10, 20, 30, 40], k = 2))
