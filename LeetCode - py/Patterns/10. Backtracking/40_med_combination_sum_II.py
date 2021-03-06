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
    1. 
  Complexity:
    Time: O()
    Space: O()
  '''
  def combinationSum2(self, candidates, target):
    candidates.sort()
    result = []
    path = []
    crrSum = 0

    def backtracking (start):
      nonlocal crrSum
      if crrSum == target:
        result.append(path[:])

      for i in range(start, len(candidates)):
        # pruning
        if crrSum + candidates[i] > target:
          continue
        if i > start and candidates[i] == candidates[i-1]:
          continue

        path.append(candidates[i])
        crrSum += candidates[i]
        backtracking(i+1)
        path.pop()
        crrSum -= candidates[i]

    backtracking(0)
    return result


## Run code after defining input and solver
input1 = [10,1,2,7,6,1,5]
input2 = 8
solver = Solution().combinationSum2
print(solver(input1, input2))