class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        j=0
        count=0
        for i in range(len(s
        )):
            if s[i]=="(" :
                count+=1
            else:
                count-=1
                if s[i-1]=="(":
                    j+=2**count
        return j
