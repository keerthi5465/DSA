class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        max_subarray = 0
        set_ele = set()
        for right in range(len(s)):
            while s[right] in set_ele:
                set_ele.remove(s[left])
                left += 1
            set_ele.add(s[right])
            max_subarray = max(max_subarray, right - left + 1)
        return max_subarray
    
k = Solution()
print(k.lengthOfLongestSubstring("pwwkew"))
