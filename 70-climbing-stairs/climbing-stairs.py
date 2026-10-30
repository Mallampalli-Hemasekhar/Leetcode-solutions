class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 1
        b = 2
        if n <= 2:
            return n
        for i in range(3, n + 1):
            c = a + b
            a = b
            b = c
        return b