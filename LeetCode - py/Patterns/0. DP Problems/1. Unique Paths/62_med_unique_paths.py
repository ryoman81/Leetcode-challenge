'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?

Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Example 3:
Input: m = 7, n = 3
Output: 28

Example 4:
Input: m = 3, n = 3
Output: 6
 
Constraints:
1 <= m, n <= 100
It's guaranteed that the answer will be less than or equal to 2 * 109.
'''


class Solution:
  '''
  MY CODE VERSION
  Thought:
    Dynamic Programming template:
      State: DP[m][n] - number of ways to move to [m+1, n+1]
      Transition: DP[m][n] = DP[m-1][n] + DP[m][n-1]
      Initial states: DP[0][j] (move in the first row); DP[i][0] (move in the first column)
  Complexity:
    Time: O(n*m)
    Space: O(n*m) - space optimization available
  '''
  def uniquePaths(self, m, n):
    # Define state
    # Initialize state at the same time with all 1s
    DP = [[1] * n for i in range(m)]

    # bottom-up to construct DP
    for i in range(1, m):
      for j in range(1, n):
        DP[i][j] = DP[i-1][j] + DP[i][j-1]
      
    return DP[m-1][n-1]


## Run code after defining input and solver
input1 = 1
input2 = 1
solver = Solution().uniquePaths
print(solver(input1, input2))