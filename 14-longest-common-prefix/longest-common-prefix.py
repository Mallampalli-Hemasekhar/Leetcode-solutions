class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        pre=strs[0]
        for i in strs[1:]:
            while not i.startswith(pre):
                pre=pre[:-1]
                if not pre:
                    return ""
        return pre
