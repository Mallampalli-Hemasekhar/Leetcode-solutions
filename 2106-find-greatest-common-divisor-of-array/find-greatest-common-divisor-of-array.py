class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mn=min(nums)
        mx=max(nums)
        for i in range(mn,0,-1):
            if mn%i==0 and mx%i==0:
                return i


         