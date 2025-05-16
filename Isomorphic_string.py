class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False

        s_to_t = {}
        t_mapped = set()

        for c1, c2 in zip(s, t):
            if c1 in s_to_t:
                if s_to_t[c1] != c2:
                    return False
            else:
                if c2 in t_mapped:
                    return False  # Prevent two keys pointing to same value
                s_to_t[c1] = c2
                t_mapped.add(c2)

        return True


k = Solution()
print(k.isIsomorphic('egg','add'))