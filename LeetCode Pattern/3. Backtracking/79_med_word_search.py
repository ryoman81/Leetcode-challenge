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
    Template:
      - State variable:
        - row index
        - column index
      - State: path[] - record current valid result along recursion
      - Choices: for directions as right, up, left, down 和走迷宫问题一样
      - Pruning: 
        1. if the next location is out of the board
        2. if the next location has been visited (as tagged of '#')
        3. if the next character is not the char in word[len(path)]
  Complexity:
    Time: O(M * N * 3^L)    - 依旧不明...
    Space: O(MN)
  '''
  def exist(self, board, word):
    path = []
    result = False
    m = len(board)
    n = len(board[0])

    def backtracking(row, col):
      ## base case: if we do find a valid path that has same length of word, it must be the answer
      if len(path) == len(word):
        nonlocal result
        result = True
        return

      ## This time, we do pruning outside the for-loop
      # 本质上, 在for-loop内剪枝, 和进入到下次recursion函数内时剪枝没有区别. 
      # prune for boundary conditions
      if not 0<=row<m or not 0<=col<n or board[row][col] == '#':
        return
      # prune for invalid sequences
      if board[row][col] != word[len(path)]:
        return

      # search in solution space of four directions
      for i,j in [[0,1], [1,0], [0,-1], [-1,0]]:
        letter = board[row][col]
        # set state
        path.append(letter)
        board[row][col] = '#'
        # do backtracking with the next location
        backtracking(row+i, col+j)
        # reset state
        path.pop()
        board[row][col] = letter

    ## we start the backtracking process at each location
    for i in range(m):
      for j in range(n):
        backtracking(i, j)
        # if we found answer starting from this location, we can return True and stop searching
        if result: return True
    # if nothing found at all return False
    return False


  '''
  MY CODE VERSION
  Thought:
    Excess time limit. We exhausted all pathes including invalid solutions
    Similar as 22, this answer is still a brute force. 
    这个解答当中, 还是没有充分运用backtracking的关键点, 剪枝并确保path当中记录的是当前正确的集合
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