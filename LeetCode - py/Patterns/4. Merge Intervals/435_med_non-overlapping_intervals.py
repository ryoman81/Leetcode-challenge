'''
Given a collection of intervals, find the minimum number of intervals
you need to remove to make the rest of the intervals non-overlapping.

Example 1:
Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.

Example 2:
Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.

Example 3:
Input: [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 
Note:
You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
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
  def eraseOverlapIntervalsOpt(self, intervals):
    return 0

  '''
  MY CODE VERSION
  Thought:
    1. Sort the intervals
    2. Loop over intervals if overlap meet remove one
    3. Use pointers. no need to remove intervals
  Complexity:
    Time: O()
    Space: O()
  '''
  def eraseOverlapIntervals(self, intervals):
    result = 0
    cmp = 0   # pointer to the comparing target

    # sort the intervals by the starting time
    intervals.sort(key= lambda itv: itv[0])

    # loop over starting from the second interval
    for i in range(1, len(intervals)):
      # if the end time of comparing target later than the starting time of indexing interval
      if intervals[cmp][1] > intervals[i][0]:
        # increment result denoting that we need to remove one interval
        result += 1
        # then consider which interval to remove
        # we choose to remove interval with late end time 
        # if comparing target has later end time, remove it and change comparing target to the current one
        if intervals[cmp][1] > intervals[i][1]:
          cmp = i
      # if no overlap then move pointer of comparing target to the current index
      else:
        cmp = i

    return result


## Run code after defining input and solver
input = [[0,2],[1,3],[2,4],[3,5],[4,6]]
solver = Solution().eraseOverlapIntervals
print(solver(input))