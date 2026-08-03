class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n
        prevPrev = 1
        prev = 2
        for i in range(2, n):
            temp = prev
            prev = prev + prevPrev
            prevPrev = temp
        return prev