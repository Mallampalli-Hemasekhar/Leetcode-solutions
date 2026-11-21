class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        count =0
        q=[]
        for i in range(len(tickets)):
            q.append(i)
        while q:
            curr=q.pop(0)

            tickets[curr]-=1
            count+=1

            if tickets[curr]>0:
                q.append(curr)

            if tickets[curr]==0 and curr==k:
                return count
        