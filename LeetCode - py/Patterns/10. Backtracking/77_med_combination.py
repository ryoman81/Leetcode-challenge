'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
You may return the answer in any order.

Example 1:
Input: n = 4, k = 2
Output: [[2,4],[3,4],[2,3],[1,2],[1,3],[1,4]]

Example 2:
Input: n = 1, k = 1
Output: [[1]]

Constraints:
1 <= n <= 20
1 <= k <= n
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
  def combine(self, n: int, k: int):
    result = []
    path = []

    def backtracking (start):
      if len(path) == k:
        result.append(path[:])
        return
      
      for i in range(start, n+1):
        # make choice
        path.append(i)
        # do recursion
        backtracking (i+1)
        # backtracking
        path.pop()
        
    backtracking(1)
    return result


## Run code after defining input and solver
input1 = 4
input2 = 2
solver = Solution().combine
print(solver(input1, input2))