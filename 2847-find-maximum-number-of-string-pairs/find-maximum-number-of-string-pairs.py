class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        c=0
        i=0
        while i < len(words):
            j = i + 1

            while j < len(words):
                if words[i] == words[j][::-1]:
                    c += 1
                j += 1

            i += 1
        return c


