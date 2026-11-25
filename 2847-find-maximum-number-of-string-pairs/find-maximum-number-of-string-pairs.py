class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        c=0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if words[i]==words[j][::-1]:
                    c+=1
        return c


