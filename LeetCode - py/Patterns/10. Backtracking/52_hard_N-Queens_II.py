'''
The n-queens puzzle is the problem of placing n queens on an n x n chessboard 
such that no two queens attack each other.
Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example 1:
Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

Example 2:
Input: n = 1
Output: 1

Constraints:
1 <= n <= 9
'''


class Solution:
  '''
  MY CODE VERSION
  Thought:
    This question is removed from my topic list
    Eaxctly the same as 51 with very minor change.
      - Here we only need a counter to record the total number
      - No need for a full matrix of board, only a sparse vector to record:
          the col index at ith row where a queen located 
  Complexity:
    Time: O()
    Space: O()
  '''
  def totalNQueens(self, n):
    # initiate a board of nxn
    result = 0
    sparse = [-1] * n

    def backtracking (row):
      if row == n:
        nonlocal result
        result += 1

      for col in range(n):
        # prune to check if this queen valide
        if not self.check(sparse, row, col):
          continue

        # if valid backtracking recursion
        sparse[row] = col
        backtracking (row+1)

        # backtracking reset the queen
        sparse[row] = -1
        
    backtracking(row=0)
    return result

  # helper that check if placing a queen on current [row, col] is valid
  def check (self, sparse, row, col):
    # check if any queen in the current column
    for i in range(0, row):
      if sparse[i] == col:
        return False
    # check if any left up position has queen
    # in C++ types: for (i=row-1, j=col-1; i>=0 && j>=0; i--, j--){}
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
      if sparse[i] == j:
        return False
    # check if any right up position has queen
    for i, j in zip(range(row-1, -1, -1), range(col+1, len(sparse), 1)):
      if sparse[i] == j:
        return False

    return True

## Run code after defining input and solver
input = 8
solver = Solution().totalNQueens
print(solver(input))