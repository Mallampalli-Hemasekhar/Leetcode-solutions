class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        for i in range(9,-1,-1):
            a=str(i)*3
            if a in num:
                return a
        return ""
