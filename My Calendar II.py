# LeetCode 731 : My Calendar II
# https://leetcode.com/problems/my-calendar-ii/description/
class MyCalendarTwo:
    
    
    def __init__(self):
        self.ranges = []
        self.overlaps = []

    def book(self, start: int, end: int) -> bool:
        for overlap in self.overlaps:
            if max(start, overlap[0]) < min(end, overlap[1]):
                return False

        for range_ in self.ranges:
            max_start = max(start, range_[0])
            min_end = min(end, range_[1])
            if max_start < min_end:
                self.overlaps.append([max_start, min_end])

        self.ranges.append([start, end])
        return True