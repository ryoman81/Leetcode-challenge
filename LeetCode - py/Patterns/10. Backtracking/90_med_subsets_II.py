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
    1. 
  Complexity:
    Time: O()
    Space: O()
  '''
  def subsets(self, nums):
    nums.sort()
    result = []
    path = []

    def backtracking (start):
      result.append(path[:])

      if start == len(nums):
        return

      for i in range(start, len(nums)):
        if i > start and nums[i] == nums[i-1]:
          continue
        path.append(nums[i])
        backtracking(i+1)
        path.pop()
        
    backtracking(0)
    return result


## Run code after defining input and solver
input1 = [1,2,2]
solver = Solution().subsets
print(solver(input1))