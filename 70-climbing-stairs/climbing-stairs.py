class Solution(object):
    def climbStairs(self, n):
        dp=[]
        for i in range(n+1):
            dp.insert(i,-1)
        return self.calculate(n,dp)
    def calculate(self,n,dp):
        if n<0:
            return 0
        if n==0:
            return 1
        if dp[n]!=-1:
            return dp[n]
        
        dp[n]=self.calculate(n-1,dp) + self.calculate(n-2,dp)

        return dp[n]