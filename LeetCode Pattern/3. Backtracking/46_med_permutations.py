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
    This is a STAR question, high frequent and I met in AMAZON!!!!!!
    But once you learned backtracking, you will see it how simple and brief
    Template:
      - State variable: used[] - record if current node has been used
      - State: path[] - record current valid result along recursion
      - Choices: all numbers in the input list
      - Pruning:
        1. if the current node has been used
  Complexity:
    Time: O(n!)   - of course as named permutation, n! is what it means
    Space: O(n)   - closure variables and the maximum recursion depth
  '''
  def permute(self, nums):
    result = []                   # result list
    path = []                     # state
    used = [False] * len(nums)    # state variable [false, false, ...]

    def backtracking ():
      # base case if the path length meet the requirement
      if len(path) == len(nums):
        result.append(path[:])
        return
      # search solution space
      for i in range(len(nums)):
        # prune used cases
        if used[i]:
          continue
        # set state for next recursion
        path.append(nums[i])
        used[i] = True
        # do recursion
        backtracking ()
        # restore state after recursion
        path.pop()
        used[i] = False
        
    backtracking()
    return result


## Run code after defining input and solver
input = [1,2,3]
solver = Solution().permute
print(solver(input))