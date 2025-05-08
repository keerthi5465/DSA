class Solution(object):
    def minDays(self, bloomDay, m, k):
        if m * k > len(bloomDay):
            return -1
        

        low = min(bloomDay)
        high = max(bloomDay)

        while low <= high:
            count = 0
            total_m = 0
            mid = (low + high) // 2
            for i in bloomDay:
                if i <= mid:
                    count += 1
                    if  count == k:
                        total_m += 1
                        count = 0
                        
                else:
                    count = 0
            if total_m >= m:
                high = mid - 1
            else:
                low =  mid + 1
                
                    
        return low


k = Solution()
print(k.minDays([1,10,3,10,2],3,1))