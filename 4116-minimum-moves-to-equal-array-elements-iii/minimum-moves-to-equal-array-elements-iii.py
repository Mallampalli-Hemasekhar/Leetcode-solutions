class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=max(nums)
        c=0
        for i in range(len(nums)):
            while nums[i]<a:
                nums[i]=nums[i]+1
                c+=1
        return c