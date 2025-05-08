class Solution:

    def aggressiveCows(self, stalls, k):
        # your code here
        arr = []
        s = sorted(stalls)
        low = 1
        high = s[-1] - s[0]
        while low <= high:
            mid = (low + high) //2
            c = 1
            last_pos = s[0]
            for i in range(1,len(s)):
                if last_pos + mid <= s[i]:
                    c += 1
                    last_pos = s[i]
                    arr.append(s[i])
            if c == k:
                low = mid + 1
                

            else:
                high = mid - 1
        return mid

k = Solution()
print(k.aggressiveCows([18,2,7],3))