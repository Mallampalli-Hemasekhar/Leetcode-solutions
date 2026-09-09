class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<1000:
            return 0
        i=0
        cur=1000
        while (cur<=n):
            i+=n-cur+1
            cur *=1000
        return i
        