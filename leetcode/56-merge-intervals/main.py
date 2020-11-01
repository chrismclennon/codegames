class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def merge_intervals(a: List[int], b: List[int]) -> List[int]:
            if a[1] >= b[0]:
                return [
                    min(a[0], b[0]),
                    max(a[1], b[1])
                ]
            return None
            
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        slow, middle, fast = 0, 0, 1
        while fast < len(intervals):
            new_interval = merge_intervals(intervals[middle], intervals[fast])
            if new_interval is not None:
                intervals[slow] = new_interval
                middle = slow
            else:
                intervals[slow] = intervals[middle]
                middle = fast
                slow += 1
            fast += 1 
        intervals[slow] = intervals[middle]
        return intervals[:slow+1]
