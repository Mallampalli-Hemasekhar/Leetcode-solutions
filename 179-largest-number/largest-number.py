class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        a = []
        for i in nums:
            a.append(str(i))
        for i in range(len(a)):
            for j in range(i + 1, len(a)):
                if a[i] + a[j] < a[j] + a[i]:
                    a[i], a[j] = a[j], a[i]

        return str(int("".join(a)))