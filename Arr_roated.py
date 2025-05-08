class Solution:
    def rotated(self,arr):
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if low < mid :
                if arr[mid - 1] < arr[mid] < arr[mid + 1]:
                    low = mid + 1
                else:
                    return mid
            elif high > mid:
                if arr[mid - 1] < arr[mid] < arr[mid + 1]:
                    high = mid - 1
                else:
                    return mid + 1
        return 0

if __name__ == "__main__":
    arr = [7, 9, 11, 12, 15]
    k = Solution()
    print(k.rotated(arr))