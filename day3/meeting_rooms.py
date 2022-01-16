"""
Given an array of meeting time intervals consisting of start and end times[[s1,e1],[s2,e2],...](si< ei), determine if a person could attend all meetings.

Example 1:

Input:
[[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input:[[7,10],[2,4]]

Output:true
"""

class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def meeting_rooms(self, meetings):
        if not meetings: return True

        meetings.sort(key=lambda x:x.start)

        for i in range(len(meetings)-1):
            if meetings[i].end > meetings[i+1].start:
                return False

        return True

if __name__ == "__main__":
    interval1 = Interval(0,14)
    interval2 = Interval(61,70)
    interval3 = Interval(15,20)
    meetings = [interval1, interval2, interval3]
    sol = Solution()
    print(sol.meeting_rooms(meetings))