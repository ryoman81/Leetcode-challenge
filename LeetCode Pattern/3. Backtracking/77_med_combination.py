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
    Template:
      - State variable: start - carried out variable, maintain the search starting index for each recursion.
      - State: path[] - record current valid result along recursion
      - Choices: all numbers from start point to the end of input array
      - Pruning:
        1. We update solution space each time entering a new recursion
  Complexity:
    Time: O(C(n,k))   - think about the defination of C^k_n= n!/( (n-k)!*k! )
    Space: O(n) 
  '''
  def combine(self, n: int, k: int):
    result = []   # result list 
    path = []     # state

    def backtracking (start):
      # base case if the current path meet the length k of the requirement
      if len(path) == k:
        result.append(path[:])
        return
      # search solution space from starting point to the end of total possible number
      for i in range(start, n+1):
        # set state for next recursion
        path.append(i)
        # do recursion
        backtracking (i+1)
        # restore state after recursion
        path.pop()
        
    backtracking(1)
    return result


## Run code after defining input and solver
input1 = 4
input2 = 2
solver = Solution().combine
print(solver(input1, input2))