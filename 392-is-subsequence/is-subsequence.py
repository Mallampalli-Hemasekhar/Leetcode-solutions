class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l=0
        r=0
        while l<len(s) and r<len(t):
            if s[l]==t[r]:
                l+=1
                r+=1
            elif s[l]!=t[r]:
                r+=1
        if l==len(s):
            return True
        return False
        
             
