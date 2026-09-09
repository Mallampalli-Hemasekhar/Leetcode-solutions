class Solution(object):
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        a=sorted(capacity,reverse=True)
        b=sum(apple)
        c=0
        s=0
        for num in a:
            s+=num
            c+=1
            if s>=b:
                break
        return c

            






