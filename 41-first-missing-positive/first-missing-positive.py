class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = []

        n = len(nums)

        for i in range(1, n + 2):
            l.append(i)
        nums_set = set(nums)

        for i in l:
            if i not in nums_set:
                return i
            