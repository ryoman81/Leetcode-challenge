'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and space is marked as 1 and 0 respectively in the grid.

Example 1:
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

Example 2:
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
 
Constraints:
m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] is 0 or 1.
'''


class Solution:
  '''
  MY CODE VERSION
  Thought:
    Dynamic Programming template:
      State: DP[m][n] - number of ways to move to [m+1, n+1]
      Transition: DP[m][n] = DP[m-1][n] + DP[m][n-1] or zero if it is an obstacle
      Initial states: DP[0][j] (move in the first row); DP[i][0] (move in the first column)
  Complexity:
    Time: O(n*m)
    Space: O(n*m) - space optimization available
  '''
  def uniquePathsWithObstacles(self, obstacleGrid):
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    # Define state DP[][] = [[0,0,...,0], ... [0,0,...,0]]
    # Initialize state at the same time
    DP = [[0] * n for i in range(m)]
    # Initialize the first row
    for i in range(n):
      if obstacleGrid[0][i] == 0:
        DP[0][i] = 1
      # Be sure that if there is an obstacle, the remaining pos are no longer accessable
      else: break
    # Initialize the first col
    for i in range(m):
      if obstacleGrid[i][0] == 0:
        DP[i][0] = 1
      # Be sure that if there is an obstacle, the remaining pos are no longer accessable
      else: break

    # bottom-up to construct DP
    for i in range(1, m):
      for j in range(1, n):
        if obstacleGrid[i][j] == 1:
          DP[i][j] = 0
        else:
          DP[i][j] = DP[i-1][j] + DP[i][j-1]
      
    return DP[m-1][n-1]


## Run code after defining input and solver
input1 = [[1],[0]]
solver = Solution().uniquePathsWithObstacles
print(solver(input1))