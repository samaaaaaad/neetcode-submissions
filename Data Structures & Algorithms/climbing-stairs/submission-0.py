from math import sqrt
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        phi = (1+sqrt(5))/2
        F_n1 = (phi**(n) - (1 - phi)**(n))/sqrt(5)
        F_n2 = (phi**(n-1) - (1 - phi)**(n-1))/sqrt(5)
        return round(F_n1) + round(F_n2)