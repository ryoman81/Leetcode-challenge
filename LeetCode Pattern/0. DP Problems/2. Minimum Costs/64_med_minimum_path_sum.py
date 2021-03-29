'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, 
which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.

Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 100
'''


class Solution:
  '''
  MY CODE VERSION
  Thought:
    Dynamic Programming template:
      State: DP[i][j] - the minimum cost sum at indexing of [i][j]
      Transition: DP[i][j] = min(DP[i-1][j], DP[i][j-1]) + grid[i][j]
      Initial states: DP[0][0] origin; DP[0][j] first row; DP[i][0] first column
  Complexity:
    Time: O(n*m)
    Space: O(n*m) - space optimization available
  '''
  def minPathSum(self, grid):
    m = len(grid)
    n = len(grid[0])
    # Create DP state with 1 x (n+1) because we include stair 0
    DP = [[0] * (n) for i in range(m)]

    # Initialize DP at origin
    DP[0][0] = grid[0][0]
    # initialize the first row of DP
    for i in range(1, m):
      DP[i][0] = DP[i-1][0] + grid[i][0]
    # initialize the first colunm of DP
    for j in range(1, n):
      DP[0][j] = DP[0][j-1] + grid[0][j]

    # Construct DP
    for i in range(1, m):
      for j in range(1, n):
        DP[i][j] = min(DP[i-1][j], DP[i][j-1]) + grid[i][j]

    return DP[m-1][n-1]


## Run code after defining input and solver
input = [[1,2,3],[4,5,6]]
solver = Solution().minPathSum
print(solver(input))