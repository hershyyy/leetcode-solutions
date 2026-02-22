# runtime: 0ms (only 8 test cases)
# time complexity: O(4^n / sqrt(n)
# space complexity: O(n)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = [(0, 0,'')]
        while stack:
            opened, closed, paren = stack.pop()
            if opened == n and closed == n:
                result.append(paren)
            if opened < n:
                stack.append((opened+1, closed, paren+'('))
            if closed < opened:
                stack.append((opened, closed+1, paren+')'))
        return result

  # originally tried creating a dp table only and iterating, but this is
  # dfs dp -> keep track of result while performing dfs
  # idea is to keep track of # of opened and closed parentheses
  #### only append closed if closed < open
  #### only append opened if opened < n
  # base case: if we have n opened and n closed, it is a valid case and we add to result
