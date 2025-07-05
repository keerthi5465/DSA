
def maxSubarray(arr):
    # Write your code here
    sub_seq = 0
    max_seq = arr[0]
    for i in arr:
        if i > 0:
            sub_seq += i
    if sub_seq == 0:
        return [max(arr),max(arr)]
    for i in range(len(arr)):
        curr_sum = 0
        for j in range(i,len(arr)):
            curr_sum += arr[j]
            max_seq = max(max_seq,curr_sum)
    return [max_seq,sub_seq]

arr = [2 ,-1, 2, 3 ,4, -5]
print(maxSubarray(arr))