def find_second_largest(arr):
    max_n = 0
    temp = 0
    l = 0
    for r in range(len(arr)):
        temp += arr[r]
        max_n = max(max_n, temp)
        if r == len(arr):
            l += 1

                
    return max_n

arr = [1,2,3,-1]
print(find_second_largest(arr))
