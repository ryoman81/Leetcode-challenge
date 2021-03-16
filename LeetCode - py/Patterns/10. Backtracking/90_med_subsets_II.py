'''
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
 
Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
'''


class Solution:
  '''
  MY CODE VERSION
  Thought:
    Template:
      - State variable: 
        - start - carry out varible to limit the solution space only from the current index
      - State: path[] - record current valid result along recursion
      - Choices: all numbers from start point to the end of input array
      - Pruning:
        1. we have update solution space every time in recursion [start, end]
        2. similar as 47 and 40, if the next item in sorted array is a duplication, skip it
  Complexity:
    Time: O(n * 2^n)
    Space: O(n)
  '''
  def subsets(self, nums):
    nums.sort()
    result = []
    path = []

    def backtracking (start):
      # update result before checking base case as prob. 78
      result.append(path[:])
      # base case
      if start == len(nums):
        return
      # search solution space from start to end
      for i in range(start, len(nums)):
        # pruning if the current node is the same as the last one
        if i > start and nums[i] == nums[i-1]:
          continue
        # set state
        path.append(nums[i])
        # do backtracking
        backtracking(i+1)
        # reset state
        path.pop()
        
    backtracking(0)
    return result


## Run code after defining input and solver
input1 = [1,2,2]
solver = Solution().subsets
print(solver(input1))