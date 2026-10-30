class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        l = 0
        c = {}
        m = 0
        for r in range(len(fruits)):
            c[fruits[r]] = c.get(fruits[r], 0) + 1
            while len(c) > 2:
                c[fruits[l]] -= 1
                if c[fruits[l]] == 0:
                    del c[fruits[l]]
                l += 1
            m = max(m, r - l + 1)
        return m