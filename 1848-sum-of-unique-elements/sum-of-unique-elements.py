class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=set()
        dup=set()
        for i in nums:
            if i in l:
                dup.add(i)
            else:
                l.add(i)
        l=l-dup
        return sum(l)
