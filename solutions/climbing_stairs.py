# runtime: 0ms
# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        prev, prevprev, curr = 1, 1, 1
        for _ in range(n-1):
            curr = prev + prevprev
            prevprev = prev
            prev = curr
        return curr
