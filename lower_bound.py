class solution:
    def lower_bound(self,arr,target):
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (high + low) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                high = mid - 1


            else:
                low = mid + 1
        return low
k = solution()
print(k.lower_bound([2, 4, 6, 8, 10], 15))