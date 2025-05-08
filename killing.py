class Solution:
    def killing(self,people):
        arr = []
        for i in range(1,people):
            arr.append(i)
        temp = 0
        while len(arr) != 1:
            temp += 1
            temp %= len(arr)
            del arr[temp]
            
            
        return arr[0]

k = Solution()
print(k.killing(6))
