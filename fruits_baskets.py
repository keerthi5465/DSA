from collections import defaultdict
class Solution(object):
    def totalFruit(self, fruits):
        dicts = defaultdict(int)
        left = 0
        max_fruits = 0
        for right in range(len(fruits)):
            dicts[fruits[right]] += 1

            while len(dicts) > 2:
                dicts[fruits[left]] -= 1
                if dicts[fruits[left]] == 0:
                    del dicts[fruits[left]]
                left += 1
            max_fruits = max(max_fruits,right - left + 1)
        return max_fruits
        
            

                
        
        

k = Solution()
print(k.totalFruit([0,1,2,2])) 
