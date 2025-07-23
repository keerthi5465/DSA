def is_jth_bit_set(n, j):
    c = 0
    while n:
        c += n & 1
        n >>= 1
    return c
    
print(is_jth_bit_set(10,1))