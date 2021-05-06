'''
Given a triangle array, return the minimum path sum from top to bottom.
For each step, you may move to an adjacent number of the row below. 
More formally, if you are on index i on the current row, 
you may move to either index i or index i + 1 on the next row.

Example 1:
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

Example 2:
Input: triangle = [[-10]]
Output: -10

Constraints:
1 <= triangle.length <= 200
triangle[0].length == 1
triangle[i].length == triangle[i - 1].length + 1
-104 <= triangle[i][j] <= 104
 
Follow up: Could you do this using only O(n) extra space, where n is the total number of rows in the triangle?
'''


class Solution:
  '''
  MY CODE VERSION
  Thought:
    Dynamic Programming template:
      State: DP[n][m] - the minimum path sum at layer n-1 and index m-1
      Transition: DP[n][i] = min(DP[n-1][i-1], DP[n-1][i]) + triangle[n][i]
      Initial states: DP[0][0]
  Complexity:
    Time: O(allNodes)
    Space: O(allNodes) - time complexity optimization available in O(n)
  '''
  def minimumTotal(self, triangle):
    n = len(triangle)
    # Create DP of n*(n+1) matrix (though easy to create than creating a triangle shape)
    DP = [[float('inf')] * (n+1) for i in range(n)]
    # Initialize DP at [0][0]
    DP[0][0] = triangle[0][0]

    # Construct DP by looping over each triangle layers starting from layer two
    for i in range(1, n):
      # iterate each node at the current layer
      for j in range(i+1):
        # if the current node is the left most node
        if j == 0:
          DP[i][j] = DP[i-1][j] + triangle[i][j]
        # if the current node is the right most node
        elif j == i:
          DP[i][j] = DP[i-1][j-1] + triangle[i][j]
        # else find the minimum path by comparing the parent nodes  
        else:
          DP[i][j] = min(DP[i-1][j-1], DP[i-1][j]) + triangle[i][j]

    # finally we return the minimum path sum at the bottom of DP
    return min(DP[n-1])


## Run code after defining input and solver
input = [[-10]]
solver = Solution().minimumTotal
print(solver(input))