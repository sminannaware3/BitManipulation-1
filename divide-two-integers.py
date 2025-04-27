# Time O(result)
# Space O(1)
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        bitshift = 0
        
        MAX_INT = 2147483647  # 2**31 - 1
        MIN_INT = -2147483648  # -2**31

        # Special case: overflow.
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        flag = False if (dividend < 0 and divisor < 0) or (dividend >= 0 and divisor >= 0) else True
        divisor = abs(divisor)
        dividend = abs(dividend)
        while dividend >= divisor:
            shift = 0
            shifteddivisor = divisor
            while shifteddivisor <= dividend:
                shifteddivisor = shifteddivisor << 1
                #print(shifteddivisor)
                shift += 1
            shift -= 1
            dividend = dividend - (divisor << shift)
            bitshift += (1 << shift)
        return -bitshift if flag else bitshift
