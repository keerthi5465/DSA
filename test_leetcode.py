class Solution(object):
    def search(self, arr, target):
        low = 0
        high = len(arr) - 1
        mid = 0
        for i in range(len(arr)):
            if low + high // 2 < high:
                mid = low + high // 2
            if arr[low] == target:
                return low
            if arr[high] == target:
                return high
            if arr[mid] != target:
                if arr[mid] > target:
                    high = mid
                elif arr[mid] < target:
                    low = mid
            
        return mid if arr[mid] == target else -1
    
k = Solution()
arr = []
target = int(input())
i = int(input())
for j in range(i):
    arr.append(int(input()))
print(k.search(arr,target))