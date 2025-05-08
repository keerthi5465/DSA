class Solution:
    def rain_water_Ascii(self,words):
        result = []
        arr = []
        for i in words:
            arr.append(ord(i))
        left_max = [0] * len(arr)
        right_max = [0] * len(arr)
        left_max[0] = arr[0]
        for i in range(1,len(arr)):
            left_max[i] = max(left_max[i - 1],arr[i])
        right_max[len(arr) - 1] = arr[len(arr) - 1]
        for i in range(len(arr) - 2, -1,-1):
            right_max[i] = max(right_max[i + 1],arr[i])
        for i in range(len(arr)):
            temp = min(left_max[i],right_max[i])
            result.append(temp - arr[i])
        return sum(result)


                        

k = Solution()
words = input()
print(k.rain_water_Ascii(words))
