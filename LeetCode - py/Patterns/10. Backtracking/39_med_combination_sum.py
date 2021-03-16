'''
Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen numbers sum to target. 
You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times. 
Two combinations are unique if the frequency of at least one of the chosen numbers is different.
It is guaranteed that the number of unique combinations that sum up to target is 
less than 150 combinations for the given input.

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []

Example 4:
Input: candidates = [1], target = 1
Output: [[1]]

Example 5:
Input: candidates = [1], target = 2
Output: [[1,1]]
 
Constraints:
1 <= candidates.length <= 30
1 <= candidates[i] <= 200
All elements of candidates are distinct.
1 <= target <= 500
'''


class Solution:
  '''
  MY CODE VERSION
  Thought:
    Template:
      - State variable: 
        - crrSum - record the current summation of all nodes in path
        - start - carry out varible to limit the solution space only from the current index
      - State: path[] - record current valid result along recursion
      - Choices: all numbers from start point to the end of input array
      - Pruning:
        1. we have update solution space every time in recursion [start, end]
        2. if current summation is greater than the target we end this path and stop keeping recursion
  Complexity:
    Time: O(n * 2^n)   - 不知道, 没仔细想
    Space: O(target)   - the maximum number of recursion when target = 1+1+...+1
  '''
  def combinationSum(self, candidates, target):
    result = []
    path = []
    crrSum = 0

    def backtracking (start):
      nonlocal crrSum
      # base case when find the target
      if crrSum == target:
        result.append(path[:])
      # search solution space
      for i in range(start, len(candidates)):
        # pruning if summation is greater than target
        if crrSum + candidates[i] > target:
          continue
        # set state
        path.append(candidates[i])
        crrSum += candidates[i]
        # comparing to 77 and 40, we do backtracking from current node since the number can be reused
        backtracking(i) 
        # restore state
        path.pop()
        crrSum -= candidates[i]

    backtracking(0)
    return result


## Run code after defining input and solver
input1 = [2,3,5]
input2 = 8
solver = Solution().combinationSum
print(solver(input1, input2))