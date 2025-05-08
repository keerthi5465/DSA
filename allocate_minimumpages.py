class Solution:
    def books_allowcations(self,arr,k):
        n = len(arr)
        
        if k > n:
            return -1
        if k == 1:
            return sum(arr)
        low = max(arr)
        high = sum(arr)
        best = high
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


            if l > k:
                
                low = mid + 1
            else:
                best = mid 
                high = mid - 1
        return best
                
k = Solution()
print(k.books_allowcations([5, 5, 5, 100], 2))