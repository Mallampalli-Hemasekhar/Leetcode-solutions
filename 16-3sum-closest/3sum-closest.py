class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest = float('inf')
        result = 0

        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]

                if abs(s - target) < closest:
                    closest = abs(s - target)
                    result = s

                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    return s   

        return result