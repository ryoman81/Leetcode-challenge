'''
Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 
Constraints:
1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
'''


class Solution:
  '''
  MY CODE VERSION
  Thought:
    Similar as 47, the number set could be duplicated, a sorting ahead is needed
    Template:
      - State variable: 
        - crrSum - record the current summation of all nodes in path
        - start - carry out varible to limit the solution space only from the current index
      - State: path[] - record current valid result along recursion
      - Choices: all numbers from start point to the end of input array
      - Pruning:
        1. we have update solution space every time in recursion [start, end]
        2. if current summation is greater than the target we end this path and stop keeping recursion
        3. if current node is the same as the last node we skip this one since it might cause path duplication
  Complexity:
    Time: O(n * 2^n)    - 同样不太明, 但是和此类题一样, 是一个宽松的上限
    Space: O(n)
  '''
  def combinationSum2(self, candidates, target):
    candidates.sort()
    result = []
    path = []
    crrSum = 0

    def backtracking (start):
      nonlocal crrSum
      # base case
      if crrSum == target:
        result.append(path[:])
      # search solution space from start to the end of array
      for i in range(start, len(candidates)):
        # pruning 1: if summation is greater than target
        if crrSum + candidates[i] > target:
          continue
        # pruning 2: if the current node is the same as the last one
        if i > start and candidates[i] == candidates[i-1]:
          continue
        # set state
        path.append(candidates[i])
        crrSum += candidates[i]
        # do backtracking and carry out a new starting point for the search space
        backtracking(i+1)
        # reset state
        path.pop()
        crrSum -= candidates[i]

    backtracking(0)
    return result


## Run code after defining input and solver
input1 = [10,1,2,7,6,1,5]
input2 = 8
solver = Solution().combinationSum2
print(solver(input1, input2))