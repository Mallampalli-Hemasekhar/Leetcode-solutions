class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l=0
        h=len(nums)-1
        while l<=h:
            mid=(l+h)//2
            if target==nums[mid]:
                return mid
            elif target < nums[mid]:
                h=mid-1
            else:
                l=mid+1
        nums.insert(l,target)
        return l
            

            