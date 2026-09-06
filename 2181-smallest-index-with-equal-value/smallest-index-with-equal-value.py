class Solution(object):
    def smallestEqual(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i, x in enumerate(nums):
            if i % 10 == x:
                return i
        return -1  