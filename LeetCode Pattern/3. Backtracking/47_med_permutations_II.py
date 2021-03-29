'''
Given a collection of numbers, nums, that might contain duplicates, 
return all possible unique permutations in any order.

Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 
Constraints:
1 <= nums.length <= 8
-10 <= nums[i] <= 10
'''


class Solution:
  '''
  MY CODE VERSION
  Thought:
    An advanced 46, the keys are:
      - Sorting the input array
      - Use pruning to avoid duplication
    Template:
      - State variable: used[] - record if current node has been used
      - State: path[] - record current valid result along recursion
      - Choices: all numbers in the input list
      - Pruning:
        1. if the current node has been used
        2*. if the current node is the duplication of the previous one
  Complexity:
    Time: O(n!)
    Space: O(n)
  '''
  def permuteUnique(self, nums):
    # sort nums list hence we can find duplicate easily
    nums.sort()

    result = []                   # result list
    path = []                     # state
    used = [False] * len(nums)    # state variable

    def backtracking ():
      # base case
      if len(path) == len(nums):
        result.append(path[:])
        return
      # search solution space of all numbers in the input array
      for i in range(len(nums)):
        # pruning
        # a) if the current node has been used and exist in state (path), or
        # b) if the current node is a duplication of the previous AND the previous one CAN BE used
        if used[i] or (i > 0 and nums[i] == nums[i-1] and not used[i-1]):
          continue
        # set state
        path.append(nums[i])
        used[i] = True
        # do backtracking
        backtracking()
        # restore state
        path.pop()
        used[i] = False

    backtracking()
    return result


## Run code after defining input and solver
input = [1,1,1,1,2]
solver = Solution().permuteUnique
print(solver(input))