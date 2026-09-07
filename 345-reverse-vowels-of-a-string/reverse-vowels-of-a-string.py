class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        l=0
        r=len(s)-1
        a=['a','e','i','o','u','A','E','I','O','U']
        b=list(s)
        while l<=r:
            if b[l] in a and b[r] in a:
                b[l],b[r]=b[r],b[l]
                l+=1
                r-=1
            elif b[r] not in a:
                r-=1
            else:
                l+=1
        return "".join(b)
            
