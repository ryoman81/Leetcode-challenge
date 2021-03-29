'''
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) 
connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
'''


class Solution:
  '''
  MY CODE VERSION
  Thought:
    Similar to problem 200. 
    In this problem, we use an additional closure variable area to record the eara of current island
    In the most answers, they pass area as argument of recursion function.
  Complexity:
    Time: O(n)
    Space: O(n)
  '''
  
  def maxAreaOfIsland(self, grid):
    maxIsland = 0
    area = 0
    m = len(grid)
    n = len(grid[0])

    def DFS(row, col):
      # base case if out boundary
      if not 0 <= row < m or not 0 <= col < n:
        return
      # base case if out island
      if grid[row][col] != 1:
        return 

      grid[row][col] = 0
      nonlocal area
      area += 1

      DFS(row+1, col)
      DFS(row-1, col)
      DFS(row, col+1)
      DFS(row, col-1)

    for i in range(m):
      for j in range(n):
        if grid[i][j] == 1:
          DFS(i, j)
          maxIsland = max(maxIsland, area)
          # please remember to reset area for the next use
          area = 0

    return maxIsland


## Run code after defining input and solver
input = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]
solver = Solution().maxAreaOfIsland
print(solver(input))