class Solution(object):
    def myAtoi(self, s):
        res = []
        r = []
        for i in range(len(s)):
            if s[i].isdigit():
                res.append(s[i])
            elif s[i] == ' ' or s[i] == '-':
                continue
            else:
                res.append('0')

        for i in range(len(res)):
            if res[i] != '0':
                r.append(res[i])
            else:
                break

        num = ''.join(r)
        n = int(num)

        return abs(n)

k = Solution()
print(k.myAtoi(" -042"))