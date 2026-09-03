class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        run_sum,max_sum=0,min(nums)
        for i in nums:
            run_sum+=i
            max_sum=max(max_sum,run_sum)
            if run_sum<0:
                run_sum=0
        return max_sum