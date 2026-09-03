class Solution(object):
    def findValidElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        right = [0] * n
        right[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], nums[i])
        left = 0
        ans = []
        for i in range(n):
            x = nums[i]
            if x > left or i == n-1 or (i < n-1 and x > right[i+1]):
                ans.append(x)
            left = max(left, x)
        
        return ans

