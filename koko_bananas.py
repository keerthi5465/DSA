class Solution(object):
    def minEatingSpeed(self, piles, h):
        if len(piles) == h:
            return max(piles)
        piles = sorted(piles)
        low = 1
        
        ams = 0
        high = max(piles)
        def totalBanana(self,arr,hour):
            total = 0
            for i in arr:
                total += (i + hour - 1) // hour
            return total
        while low <= high:
            mid = (low + high) // 2
            t = totalBanana(self,piles,mid)
            if t <= h:
                high = mid - 1
            else:
                low = mid + 1
        return low 

k = Solution()
print(k.minEatingSpeed([3,6,7,11],8))