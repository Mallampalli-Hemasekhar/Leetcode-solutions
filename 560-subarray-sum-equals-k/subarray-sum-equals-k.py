class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix_sum = 0
        count = 0
        mp = {0: 1}

        for num in nums:
            prefix_sum += num

            if prefix_sum - k in mp:
                count += mp[prefix_sum - k]

            mp[prefix_sum] = mp.get(prefix_sum, 0) + 1

        return count
