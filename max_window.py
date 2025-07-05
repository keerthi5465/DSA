class Solution:
    def max_element(self,arr, k):
        n = len(arr)
        if k > n or k == 0:
            return []

        max_ele = []

        for i in range(n - k + 1):
            window = arr[i:i + k]
            max_in_window = max(window)
            max_ele.append(max_in_window)

        return max_ele

k = Solution()
print(k.max_element([1,2,3,4,5],3))
            