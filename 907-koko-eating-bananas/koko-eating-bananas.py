class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        low=1
        high=max(piles)
        ans=high
        while low<=high:
            mid=(low+high)//2
            hours=sum(math.ceil(pile/float(mid))for pile in piles)
            if hours<=h:
                ans=min(ans,mid)
                high=mid-1   
            else:
                low=mid+1
        return ans

    