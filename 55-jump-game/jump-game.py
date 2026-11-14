class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a= 0

        for i in range(len(nums)):
            if i > a:
                return False
            if i + nums[i] > a:
                a = i + nums[i]

        return True
        