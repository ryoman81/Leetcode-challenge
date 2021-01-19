'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Example 3:
Input: intervals = [], newInterval = [5,7]
Output: [[5,7]]
 
Constraints:
0 <= intervals.length <= 104
intervals[i].length == 2
0 <= intervals[i][0] <= intervals[i][1] <= 105
intervals is sorted by intervals[i][0] in ascending order.
newInterval.length == 2
0 <= newInterval[0] <= newInterval[1] <= 105
'''


class Solution:
  '''
  THE OPTIMAL CODE VERSION
  Improvement:
    1.
  Thought:
    1.  
  Complexity:
    Time: O()
    Space: O()
  '''
  def insertOpt(self, intervals, newInterval):
    return 0

  '''
  MY CODE VERSION
  Thought:
    1. 
  Complexity:
    Time: O()
    Space: O()
  '''
  def insert(self, intervals, newInterval):
    # check if empty of intervals
    if len(intervals) == 0:
      return [newInterval]

    result = []   # result array
    crr = 0       # current pointer
    # loop over the intervals
    # if the end time of current interval is less than the start time of new interval
    while crr < len(intervals) and intervals[crr][1] < newInterval[0]:
      result.append(intervals[crr])
      crr += 1
    
    # now we meet a potential overlap between current interval and new interval
    # loop over from current interval until the end time of new interval is larger than the start time of current interval
    while crr < len(intervals) and newInterval[1] >= intervals[crr][0]:
      # if not meet the requirement then merge then and update new interval
      newInterval[0] = min(newInterval[0], intervals[crr][0])
      newInterval[1] = max(newInterval[1], intervals[crr][1])
      crr += 1
    # once out the while loop append this merged new interval to the result list
    result.append(newInterval)
    
    # fill in the remaining time intervals to the result
    while crr < len(intervals):
      result.append(intervals[crr])
      crr += 1
    
    # return result
    return result


## Run code after defining input and solver
input1 = [[1,3],[6,9]]
input2 = [2,5]
solver = Solution().insert
print(solver(input1, input2))