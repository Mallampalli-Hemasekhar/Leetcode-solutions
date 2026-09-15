class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        seen = set()
        i, j = 0, len(nums) - 1
        while i < j:
            avg = (nums[i] + nums[j]) / 2
            seen.add(avg)
            i += 1
            j -= 1
        return len(seen)