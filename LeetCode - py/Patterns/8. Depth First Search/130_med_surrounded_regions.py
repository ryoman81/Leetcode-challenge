'''
Given an m x n matrix board containing 'X' and 'O', capture all regions surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example 1:
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. 
Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. 
Two cells are connected if they are adjacent cells connected horizontally or vertically.

Example 2:
Input: board = [["X"]]
Output: [["X"]]
 
Constraints:
m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
'''


class Solution:
  '''
  MY CODE VERSION
  Thought:
    
  Complexity:
    Time: O(n)
    Space: O()
  '''
  
  def solve(self, board) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    m = len(board)
    n = len(board[0])
    
    def DFS(row, col):
      # base case if out boundary
      if row < 0 or row >= m or col < 0 or col >= n:
          return
      # base case if meet X or tag Y
      if board[row][col] == 'X' or board[row][col] == 'Y':
          return
      
      # tage border connected O region to a temp, say Y
      board[row][col] = 'Y'
      # recursion step
      DFS(row+1, col)
      DFS(row, col+1)
      DFS(row, col-1)
      DFS(row-1, col)
        
    # travel on border and tag all border connected O to Y
    for i in range(m):
      DFS(i, 0)
      DFS(i, n-1)
    for j in range(n):
      DFS(0, j)
      DFS(m-1, j)
        
    # after retagging, let traverse all element and do flipping and restoring
    for i in range(m):
      for j in range(n):
        if board[i][j] == 'Y':
          board[i][j] = 'O'
        elif board[i][j] == 'O':
          board[i][j] = 'X'


## Run code after defining input and solver
input = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
solver = Solution().solve
solver(input)
print(input)