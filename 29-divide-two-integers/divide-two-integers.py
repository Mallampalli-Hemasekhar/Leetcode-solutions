class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        a = abs(dividend)
        b = abs(divisor)
        count = 0
        while a >= b:
            temp = b
            c = 1
            while a >= temp + temp:
                temp += temp
                c += c
            a -= temp
            count += c
        if (dividend < 0) != (divisor < 0):
            count = -count
        return min(max(count, -2147483648), 2147483647)