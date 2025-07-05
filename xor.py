def countSubarraysWithZeroXOR(arr,k):
    n = len(arr)
    max_xor = float('-inf')
    
    for i in range(n):
        xorSum = 0
        for j in range(i, n):
            xorSum ^= arr[j]
            max_xor = max(max_xor, xorSum)
    
    return max_xor
arr = [1,2,3,3,2]
k = 6
print(countSubarraysWithZeroXOR(arr,k))