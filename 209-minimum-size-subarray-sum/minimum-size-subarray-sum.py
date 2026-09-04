class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l=0
        r=0
        s=0
        min_len=float('inf')

        while r<len(nums):
            s+=nums[r]
            while s>=target:
                length=r-l+1
                min_len= length if length<min_len else min_len

                s-=nums[l]
                l+=1
            r+=1
        return min_len if min_len!=float('inf') else 0