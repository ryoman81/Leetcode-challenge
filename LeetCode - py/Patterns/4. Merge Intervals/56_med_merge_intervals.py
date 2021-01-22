'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 
Constraints:
1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
'''


class Solution:
  '''
  THE OPTIMAL CODE VERSION
  Improvement:
    Just a code simplification from my code
    Also sorted the intervals in palce to save space
  Thought:
    1. Ascend sort the starting time of each interval
    2. Merge intervals one by one by comparing the end time 
  Complexity:
    Time: O(nlogn)  sorting cmplx
    Space: O(n)
  '''
  def mergeOpt(self, intervals):
    if len(intervals) < 2:
      return intervals
    # sort the intervals in place
    intervals.sort(key=lambda itv: itv[0])
    result = []
    # instead of using pointers, using Python indexing and for loop
    for itv in intervals:
      # if the current result interval cannot be merged
      #js code: if (result.length===0) || result[result.length-1][1]<itv[0]{...}
      if len(result)==0 or result[-1][1] < itv[0]:
        result.append(itv)
      else:
        result[-1][1] = max(result[-1][1], itv[1])
    # return result
    return result
    
  '''
  MY CODE VERSION
  Thought:
    As above
  Complexity:
    Time: O(nlogn)
    Space: O(n)
  '''
  def merge(self, intervals):
    if len(intervals) < 2:
      return intervals
    # sort the inverval list by the starting time
    intervals_sorted = sorted(intervals, key=lambda interval: interval[0])

    p_org = 1     # index pointer to the sorted list
    p_des = 0     # index pointer to the destination (result) list
    result = [intervals_sorted[0]]   # result array
    while p_org < len(intervals_sorted):
      # check the next interval can be merged
      if result[p_des][1] >= intervals_sorted[p_org][0]:
        # if the current interval can be merged into the existing interval
        result[p_des][1] = max(result[p_des][1], intervals_sorted[p_org][1])
      else:
        result.append(intervals_sorted[p_org])
        p_des += 1
      # move pointer of sorted list forward
      p_org += 1
    # return result list
    return result


## Run code after defining input and solver
input = [[1,3],[2,6],[8,10],[15,18]]
solver = Solution().mergeOpt
print(solver(input))