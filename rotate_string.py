class Solution(object):
    def rotateString(self, s, goal):
        sl = len(s)
        gl = len(goal)
        if sl != gl:
            return False
        k = sl
        l = 0
        res = ""
        for i in range(len(s)):
            if s[0]== goal[i]:
                l = i
                k = i
        for i in range(len(goal)):
            


        return True if k == l else False
                
            
    
k = Solution()
print(k.rotateString("abcde","abced"))