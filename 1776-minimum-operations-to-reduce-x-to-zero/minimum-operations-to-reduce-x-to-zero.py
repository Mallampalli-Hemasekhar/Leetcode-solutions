class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        total = sum(nums)
        target = total - x

        if target == 0:
            return len(nums)

        left = 0
        s = 0
        maximum = -1

        for right in range(len(nums)):
            s += nums[right]

            while s > target and left <= right:
                s -= nums[left]
                left += 1

            if s == target:
                maximum = max(maximum, right - left + 1)

        if maximum == -1:
            return -1

        return len(nums) - maximum