from math import factorial
class Solution:
    def climbStairs(self, n: int) -> int:
        combinations = 1
        remaining_ones = n

        while (remaining_ones>=2):
            remaining_ones-= 2
            n_ones = remaining_ones
            n_twos= (n-remaining_ones) // 2
            combinations_iter= factorial(n_ones+n_twos) // ( factorial(n_twos) * factorial(n_ones) )
            combinations+= combinations_iter
        return  combinations

