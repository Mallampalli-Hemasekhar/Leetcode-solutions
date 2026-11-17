class Solution(object):
    def maximizeSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        i=0
        sum=0
        b=len(nums)-1
        while i<k:
            sum+=nums[b]+i
            i+=1
        return sum

        