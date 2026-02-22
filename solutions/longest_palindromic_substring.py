# runtime: 251 ms
# time complexity: O(n^2) -> worst case we expand center n times for n centers
# space complexity: O(1) -> just variables

class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = s[0]

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        
        for i in range(len(s)-1):
            odd = expand(i, i)
            even = expand(i, i+1)
            if len(odd) > len(even) and len(odd) > len(longest):
                longest = odd
            if len(even) > len(odd) and len(even) > len(longest):
                longest = even
        return longest
