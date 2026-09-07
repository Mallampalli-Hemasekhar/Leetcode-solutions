class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0
        rc=0
        for i in range(len(nums)):
            if nums[i]==1:
                l+=1
                rc=max(rc,l)
            else:
                l=0
        return rc

