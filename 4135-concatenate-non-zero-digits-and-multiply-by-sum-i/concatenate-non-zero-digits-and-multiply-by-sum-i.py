class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        l=list(str(n))
        for i in range(len(l)-1,-1,-1):
            if l[i]=='0':
                l.pop(i)
        if not l:
            return 0
        b=sum(map(int,l))
        c="".join(l)
        e=int(c)*b
        return e
            