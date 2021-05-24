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

import math

class Solution:
  '''
  Problem Definition:
    无限背包问题的转换
      - 构建一个篮子 [0^2, 1^2, 2^2, ... sqrt(n)^2]
      - 从该篮子中选择最少item数量使其相加为n
      - 转换成题322零钱兑换问题
  Problem Desc:
    Type: Unbounded Knapsack 无限背包问题
    Prob: Minimum number of items 最值问题
  Template:
    DP[j]: the minimum number of items needed if achieve capacity of j
    Transition: DP[j] = min(DP[j], DP[j-item] + 1)
    Initial: DP=INF, DP[0]=0
    Loop: 外层平方数的篮子, 内层capacity正序
  Complexity:
    Time: O(n * sqrt(n))
    Space: O(n)
  '''
  def numSquares(self, n):
    # define the items array
    sqrs = [i**2 for i in range(int(math.sqrt(n))+1)]
    # define the target capacity
    capacity = n

    # initiate DP
    DP = [float('inf')] * (capacity+1)
    # when the target combination sum is 0, there is 0 item needed
    DP[0] = 0

    # loop to create DP
    for item in sqrs:
      for j in range(1, capacity+1):
        # boundary condition
        if j >= item:
          DP[j] = min(DP[j], DP[j-item]+1)
    
    # return DP[capacity] as problem required
    return DP[capacity]


## Run code after defining input and solver
input = 13
solver = Solution().numSquares
print(solver(input))