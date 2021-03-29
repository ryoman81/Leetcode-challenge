'''
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle.
Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:
Input: n = 1
Output: [["Q"]]
'''


class Solution:
  '''
  MY CODE VERSION
  Thought:
    My original thought was about searching in 2D matrix (each time has choice to move to four directions)
    But that idea finally fell into brute force at all. 就跟22, 79一样, 没有利用到backtracking的精髓, 维护一个始终valid的path
    This answer practiced the standard backtracking template as
    - State variable: row - the index of current row
    - State: board[][] - record current valid result along recursion
    - Choices: n locations in a row to put on a queen
    - Pruning: 
      1. if the current queen can check all placed queens in the rows above

    ** 这个题还需要再做, 因为有优化的途径, 就是不需要每次调用check函数来判断是否valid, 需要DP来记录之前摆放queens的位置来考虑优化验证的过程.
  Complexity:
    Time: O(N!)     - still not sure about it
    Space: O(n^2)
  '''
  def solveNQueens(self, n):
    # initiate a board of nxn
    result = []
    # initialize a 2D matrix in python; [['.','.','.'], ['.','.','.'], ['.','.','.']] if n = 3
    board = [['.']*n for i in range(n)]

    def backtracking (row):
      # base case if we have put the last queen on the board
      if row == n:
        result.append(self.convert(board))
      # search for the solution space
      for col in range(n):
        # prune to check if this queen valide
        if not self.check(board, row, col):
          continue
        # set state if valid
        board[row][col] = 'Q'
        # do backtracking with the next row index
        backtracking (row+1)
        # backtracking reset the queen
        board[row][col] = '.'
        
    backtracking(row=0)
    return result

  # helper that check if placing a queen on current [row, col] is valid
  def check (self, board, row, col):
    # check if any queen in the current column
    for i in range(0, row):
      if board[i][col] == 'Q':
        return False
    # check if any left up position has queen
    # in C++ types: for (i=row-1, j=col-1; i>=0 && j>=0; i--, j--){}
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
      if board[i][j] == 'Q':
        return False
    # check if any right up position has queen
    for i, j in zip(range(row-1, -1, -1), range(col+1, len(board), 1)):
      if board[i][j] == 'Q':
        return False

    return True

  # helper that convert a 2D matrix to the desired format
  def convert(self, matrix):
    stringMatrix = []
    for row in matrix:
      newRow = ''
      for char in row:
        newRow += char
      stringMatrix.append(newRow)
    return stringMatrix

## Run code after defining input and solver
input = 4
solver = Solution().solveNQueens
print(solver(input))