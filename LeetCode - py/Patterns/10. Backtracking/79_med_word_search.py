'''
Given an m x n gird of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, 
where adjacent cells are horizontally or vertically neighboring. 
The same letter cell may not be used more than once.
Note: There will be some test cases with a board or a 
      word larger than constraints to test if your solution is using pruning.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 
Constraints:
m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
'''


class Solution:
  '''
  MY CODE VERSION
  Thought:
    
  Complexity:
    Time: O()
    Space: O()
  '''
  def exist(self, board, word):
    path = []
    result = False
    m = len(board)
    n = len(board[0])

    def backtracking(row, col):
      if len(path) == len(word):
        nonlocal result
        result = True
        return

      # prune for boundary conditions
      if not 0<=row<m or not 0<=col<n or board[row][col] == '#':
        return
      # prune for invalid sequences
      if board[row][col] != word[len(path)]:
        return

      for i,j in [[0,1], [1,0], [0,-1], [-1,0]]:
        letter = board[row][col]
        path.append(letter)
        board[row][col] = '#'
        backtracking(row+i, col+j)
        path.pop()
        board[row][col] = letter

    for i in range(m):
      for j in range(n):
        backtracking(i, j)
        if result: return True

    return False


  '''
  MY CODE VERSION
  Thought:
    Excess time limit. we must prune within backtracking function
  Complexity:
    Time: O()
    Space: O()
  '''
  def exist2(self, board, word):
    path = []
    result = False
    m = len(board)
    n = len(board[0])

    def backtracking(row, col):
      if ''.join(path) == word:
        nonlocal result
        result = True

      if not 0<=row<m or not 0<=col<n or board[row][col] == '#':
        return

      for i,j in [[0,1], [1,0], [0,-1], [-1,0]]:
        letter = board[row][col]
        path.append(letter)
        board[row][col] = '#'
        backtracking(row+i, col+j)
        path.pop()
        board[row][col] = letter

    for i in range(m):
      for j in range(n):
        backtracking(i, j)
        if result: return True

    return False

## Run code after defining input and solver
input1 = [["b","b","a","a","b","a"],["b","b","a","b","a","a"],["b","b","b","b","b","b"],["a","a","a","b","a","a"],["a","b","a","a","b","b"]]
input2 = "abbbababaa"
solver = Solution().exist
print(solver(input1, input2))