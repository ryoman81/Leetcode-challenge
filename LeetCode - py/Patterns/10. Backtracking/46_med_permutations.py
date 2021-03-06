'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]

Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
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
  def permute(self, nums):
    result = []
    path = []
    used = [False] * len(nums)

    def backtracking ():
      if len(path) == len(nums):
        result.append(path[:])
        return
      
      for i in range(len(nums)):
        # prune
        if used[i]:
          continue
        # make choice
        path.append(nums[i])
        used[i] = True
        # do recursion
        backtracking ()
        # backtracking
        path.pop()
        used[i] = False
        
    backtracking()
    return result


## Run code after defining input and solver
input = [1,2,3]
solver = Solution().permute
print(solver(input))