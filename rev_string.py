class Solution(object):
    def reverseWords(self, s):
        arr = []
        k = ""
        for i in s:
            arr.append(i)
        res = arr[::-1]
        return res
k = Solution()
print(k.reverseWords("the sky is blue"))
        

        