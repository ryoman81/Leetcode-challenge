'''
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, 
it is the product of some integer with itself. 
For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

Example 1:
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

Constraints:
1 <= n <= 104
'''


class Solution:
  '''
  MY CODE VERSION
  Thought:
    Type: 
    Definition: 
      - 
    DP template:
      - DP[j]: the least number of perfect square given the sum of j
      - Transition: DP[j] = min(DP[j-ps[i]]) + 1
        -> 
      - Init: 
  Complexity:
    Time: O()
    Space: O()
  '''
  def numSquares(self, n):
    ps = [i**2 for i in range(0, 101)]
    DP = [float('inf')] * (n+1)
    DP[0] = 0

    for i in range(1, n+1):
      for j in ps:
        if i - j >= 0:
          DP[i] = min(DP[i], DP[i-j]+1)

    return DP[n]

## Run code after defining input and solver
input = 2
solver = Solution().numSquares
print(solver(input))