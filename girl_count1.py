def func(n):
    arr = [i for i in range(5)]
    curr_num = 1
    index = 0
    flag = 0
    while curr_num<n:
        while flag==0:
            arr[index] = curr_num
            curr_num+=1
            if index == 4:
                flag = 1
            else:
                index+=1
            if n in arr:
                return arr.index(n)
        index-=1
        while flag==1:
            arr[index] = curr_num
            curr_num+=1
            if index == 0:
                flag = 0
            else:
                index-=1
            if n in arr:
                return arr.index(n)
        index+=1

n = 22
print(func(15))