class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        a=list(stones)
        while len(a)>1:
            a.sort()
            x=a.pop()
            y=a.pop()

            if x!=y:
                a.append(-(y-x))
        return a[0] if a else 0