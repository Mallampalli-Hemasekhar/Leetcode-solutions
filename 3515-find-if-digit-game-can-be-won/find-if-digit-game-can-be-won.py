class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s_d=[]
        m_d=[]
        for i in nums:
            if 0<=i<=9:
                s_d.append(i)
            else:
                m_d.append(i)
        if sum(s_d)>sum(m_d) or sum(m_d)>sum(s_d):
            return True
        return False
