'''
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
 
Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
'''


class Solution:
  '''
  MY CODE VERSION
  Thought:
    Template:
      - Almost the same as question to 77. combination
      - We need to update result ANYTIME when we enter this recursion
  Complexity:
    Time: O(n * 2^n)    - comparing to 46 and 77, this time complexity is more of a mathematical question. I copied it from official solution. 
    Space: O(n)
  '''
  def subsets(self, nums):
    result = []
    path = []

    def backtracking (start):
      # the subset requires anytime when recursion, it is one of the result
      result.append(path[:])
      # base case
      if start == len(nums):
        return
      # search solution space
      for i in range(start, len(nums)):
        path.append(nums[i])
        backtracking(i+1)
        path.pop()
        
    backtracking(0)
    return result


## Run code after defining input and solver
input1 = [1,2,3]
solver = Solution().subsets
print(solver(input1))