class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        l = 0
        s = 0
        maxi = float('-inf')

        for r in range(len(nums)):
            s += nums[r]
            if (r - l + 1) == k:
                maxi = max(maxi, float (s)/ k)    
                s -= nums[l]
                l += 1
        return float(maxi)
