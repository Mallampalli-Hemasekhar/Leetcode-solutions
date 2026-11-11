class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        a=float('inf')
        b=[]
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i]==list2[j]:
                    k=i+j
                    if k<a:
                        a=k
                        b=[list1[i]]
                    elif k==a:
                        b.append(list1[i])
        return b
