
def max_heapify(arr, n, i):
    l = i
    left = 2 * i + 1
    right = 2 * i + 2 
    if left < n and arr[left] > arr[l]:
        l = left
    if right < n and arr[right] > arr[l]:
        l = right
    if l != i:
        arr[i], arr[l] = arr[l], arr[i]
        max_heapify(arr, n, l)
def max_heap(arr):
    n = len(arr)
    for i in range(n //2 -1,-1,-1):
        max_heapify(arr,n,i)
    return arr
def delete_max(arr):
    n = len(arr)
    arr[0] = arr[n - 1] 
    arr.pop()        
    max_heapify(arr, len(arr), 0)
       

arr = [10, 100, 50, 20, 15, 18]
max_heap(arr)
delete_max(arr)
print(arr)
