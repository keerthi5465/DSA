class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self, arr, x):
        #Your code here
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == x:
                return mid + 1
            elif arr[mid] > x:
                high = mid - 1
            else:
                low = mid + 1
        return low - 1 

k = Solution()
print(k.findFloor([2],6))