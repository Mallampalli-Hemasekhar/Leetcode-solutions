class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        i=0
        j=int(c ** 0.5)
        while i<=j:
            sum=(i*i)+(j*j)
            if sum==c:
                return True
            elif sum<c:
                i+=1
            else:
                j-=1

        return False
            
            
            