
def equalStacks(h1, h2, h3):
    # Write your code here
    def pop_value(a):
        h = []
        sum_c = sum(a)
        for i in range(len(a)):
            
            h.append(sum_c)
            sum_c -= a[i]
            
        return h
    h_o = pop_value(h1)
    h_s = pop_value(h2)
    h_t = pop_value(h3)
    
    common = set(h_o) & set(h_s) & set(h_t)
    if common:
        return max(common)


    


h1 = [3, 2, 1, 1, 1]
h2 = [4, 3, 2]
h3 = [1, 1, 4, 1]
print(equalStacks(h1,h2,h3))