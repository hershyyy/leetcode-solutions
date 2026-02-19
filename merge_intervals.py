# 56. merge intervals
# runtime 7ms
# time complexity: O(nlog(n)) where n = len(intervals) -> due to sorting O(nlog(n)) and iterating in O(n)
# space complexity: O(n), worst case results array = len(intervals)

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()
        result = [intervals[0]]
        for i in range(len(intervals)):
            if result[-1][1] >= intervals[i][0]:
                result[-1][1] = max(intervals[i][1], result[-1][1])
            else:
                result.append(intervals[i])
        return result
