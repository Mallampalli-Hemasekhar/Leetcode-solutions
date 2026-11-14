class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        a = [0] * len(temperatures)

        for j in range(len(temperatures) - 1, -1, -1):
            i = j + 1
            while i < len(temperatures) and temperatures[j] >= temperatures[i]:
                if a[i] == 0:
                    i = len(temperatures)
                    break
                i += a[i]

            if i < len(temperatures):
                a[j] = i - j

        return a



            
