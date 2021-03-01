'''
Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 
Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
'''


class Solution:
  '''
  MY CODE VERSION
  Thought:
    The MOST classic and popular problem! It has the soul for many 2D DFS application problems
    In the main function:
      - Loop over all elements in 2D matrix
      - If the current element is '1', we start DFS
        - In DFS, we traversal all connected '1's in four directions
        - Every time we have been through a '1', we tag it '0'. Then next time, it will not be revisited
      - After DFS, we have traverse an entire island (and also tag it to '0'), we increment result by 1
  Complexity:
    Time: O(n)
    Space: O(n) expense for recursion steps
  '''
  
  def numIslands(self, grid):
    if not grid:
      return 0
    
    m = len(grid)
    n = len(grid[0])
    nIslands = 0
    
    def DFS(row, col):
      # base case if out boundary
      if row < 0 or row >= m or col < 0 or col >= n:
          return
      # base case if out island
      if grid[row][col] != "1":
          return

      # otherwise first altered the current land
      grid[row][col] = "0"
      # 2D matrix recursion
      DFS(row+1, col)
      DFS(row, col+1)
      DFS(row, col-1)
      DFS(row-1, col)
    
    for i in range(m):
      for j in range(n):
        if grid[i][j] == "1":
          nIslands += 1
          DFS(i, j)
    
    return nIslands


## Run code after defining input and solver
input = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
solver = Solution().numIslands
print(solver(input))