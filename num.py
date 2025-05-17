class Solution(object):
    def myAtoi(self, s):
        res = []
        r = []
        num = 0
        for i in range(len(s)):
            if s[i].isdigit() or s[i] == '-' or s[i] == '+':
                res.append(s[i])
            elif s[i] == ' ':
                continue
            else:
                res.append(' ')

        for i in res:
            if i.isdigit() or i == '-' or i == '+':
                r.append(i)
            else:
                break
        num_str = ''.join(r)
        try:
            num = int(num_str)
        except ValueError:
            num = 0
        return num

k = Solution()
print(k.myAtoi("+1"))