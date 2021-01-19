'''
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
determine if a person could attend all meetings.

Example 1:
Input: [[0,30],[5,10],[15,20]]
Output: false

Example 2:
Input: [[7,10],[2,4]]
Output: true
'''


class Solution:
  '''
  MY CODE VERSION
  Thought:
    - This problem is an easy version of 56. merge intervals. 
    - Similar steps, but only need to determine if overlapped
    - Sort by starting time and then loop over to check if overlap
    - Since no result of merged intervals to be output, the space cmplx is constant
  Complexity:
    Time: O(nlogn)
    Space: O(1)
  '''
  def canAttendMeetings(self, intervals):
    # sort intervals by the starting time
    intervals.sort(key=lambda itv: itv[0])
    # loop over intervals and check if the next starting time is earlier than the current end time
    for i in range(1, len(intervals)):
      if intervals[i][0] < intervals[i-1][1]:
        return False
    return True


## Run code after defining input and solver
input = [[7,10],[2,4]]
solver = Solution().canAttendMeetings
print(solver(input))