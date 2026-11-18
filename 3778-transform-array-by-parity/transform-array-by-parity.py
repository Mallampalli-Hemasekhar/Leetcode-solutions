class Solution(object):
    def transformArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
         
        for i,x in enumerate(nums):
            if x%2==0:
                nums[i]=0
            else:
                nums[i]=1
        return sorted(nums)