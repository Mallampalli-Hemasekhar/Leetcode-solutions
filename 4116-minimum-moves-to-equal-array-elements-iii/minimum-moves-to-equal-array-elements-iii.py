class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=max(nums)
        c=0
        for i in nums:
            c+=(a-i)
        return c
            