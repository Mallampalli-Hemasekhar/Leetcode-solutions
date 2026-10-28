class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        b = [[]]
        for i in range(len(nums)):
            n = len(b)
            for j in range(n):
                b.append(b[j] + [nums[i]])
        return b