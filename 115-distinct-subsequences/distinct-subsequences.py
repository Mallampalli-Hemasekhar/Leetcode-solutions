class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        n = len(t)
        dp = [0] * (n + 1)
        dp[0] = 1

        for ch in s:
            for j in range(n - 1, -1, -1):  
                if ch == t[j]:
                    dp[j + 1] += dp[j]

        return dp[n]



    
        