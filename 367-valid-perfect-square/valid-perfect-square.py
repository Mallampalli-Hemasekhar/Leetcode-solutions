class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        n=1
        while n*n<=num:
            if n*n==num:
                return True
            n+=1
        return False