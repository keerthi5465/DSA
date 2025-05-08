class Solution:
    def reverse_string_words(self,words):
        arr = []
        for i in words.split():
            arr.append(i[::-1])
        return (' ').join(arr)

k = Solution()
l = input()
print(k.reverse_string_words(l))
    
