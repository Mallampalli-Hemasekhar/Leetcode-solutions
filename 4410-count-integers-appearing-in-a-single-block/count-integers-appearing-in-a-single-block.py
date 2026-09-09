class Solution(object):
    def countSpecialIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        block_count = Counter()
      
        for i, x in enumerate(nums):
            if i == 0 or nums[i] != nums[i-1]:
                block_count[x] += 1 
        return sum(v == 1 for v in block_count.values())
            
        
            
            
        