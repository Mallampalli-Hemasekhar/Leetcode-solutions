class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        m=max(piles)
        for i in piles:
            if i%m==0:
                return True
        return False