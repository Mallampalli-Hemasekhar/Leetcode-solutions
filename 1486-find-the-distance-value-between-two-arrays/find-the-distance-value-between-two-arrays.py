class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        c=0
        for i in arr1:
            flag=True
            for j in arr2:
                a=abs(i-j)
                if a<=d:
                    flag=False
                    break
            if flag:
                c+=1
        return c