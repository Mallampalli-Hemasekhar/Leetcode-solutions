class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i,c,k=0,0,0
         
        while i < len(s):
            if s[i] == "(":
                c += 1
            elif s[i] == "*":
                k += 1
            else:
                if c > 0:
                    c -= 1
                elif k > 0:
                    k -= 1
                else:
                    return False
            i += 1
        i = len(s) - 1
        b,k=0,0
        while i >= 0:
            if s[i] == ")":
                b += 1
            elif s[i] == "*":
                k += 1
            else:
                if b > 0:
                    b -= 1
                elif k > 0:
                    k -= 1
                else:
                    return False
            i -= 1
        return True
 
