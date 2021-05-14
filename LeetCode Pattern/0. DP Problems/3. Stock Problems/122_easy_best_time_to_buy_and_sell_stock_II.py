'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
Find the maximum profit you can achieve. You may complete as many transactions as you like 
(i.e., buy one and sell one share of the stock multiple times).
Note: You may not engage in multiple transactions simultaneously 
(i.e., you must sell the stock before you buy again).

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

Example 2:
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.

Example 3:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e., max profit = 0.
 
Constraints:
1 <= prices.length <= 3 * 104
0 <= prices[i] <= 104
'''


class Solution:
  '''
  SPACE OPTIMIZED VERSION
    This solution is exactly the solution from LeetCode
    Modified from the space optimized version
    - DP0 --> maxProfit   :: 最大化收益
    - DP1 --> null        :: 这里同样做了变换, 隐形表示了DP1和DP0的关系
  Complexity:
    Time: O(n)
    Space: O(1)
  '''
  def maxProfit(self, prices):
    maxProfit = 0
    for i in range(1, len(prices)):
      maxProfit = max(0, prices[i]-prices[i-1]) + maxProfit
    return maxProfit

  '''
  SPACE OPTIMIZED VERSION
    since both DP0 and DP1 rely only on the previous state
    因此DP当中常见的传统的空间优化可以实施, 将DP0[i] 和 DP1[i]用单个变量表达
  Complexity:
    Time: O(n)
    Space: O(1)
  '''
  def maxProfit0(self, prices):
    n = len(prices)
    DP0 = 0
    DP1 = -prices[0]

    for i in range(1, n):
      temp = DP0
      DP0 = max(DP0, DP1+prices[i])
      DP1 = max(DP1, temp-prices[i])
    
    return DP0

  '''
  OPTIMIZED VERSION
    Similar like 121, there is no need to maintain the dimension of k
    since [k] and [k-1] should have no influence on final DP
    Lets think about the state transition and initialization
      - Transition: 
        DP0 relies on the previous DP0 or DP1 no matter what k is
          所以直接把k这个维度去除掉就可以了
        DP1 relies previous DP1[k] or DP0[k-1]. However, since k=1
          如果DP1是从前一个DP0转移过来, 则前一个DP0一定为0. 动脑筋
  Complexity:
    Time: O(n)
    Space: O(2n)
  '''
  def maxProfit1(self, prices):
    n = len(prices)
    # both DP0 and DP1 are only related to the variable of day
    DP0 = [0] * n
    DP1 = [0] * n

    # initialize DP0 DP1 at i=0
    # think that if we hold a stock at i=0
    DP1[0] = -prices[0]

    # Loop
    for i in range(1, n):
      DP0[i] = max(DP0[i-1], DP1[i-1] + prices[i])
      DP1[i] = max(DP1[i-1], -prices[i])
    
    return DP0[n-1]

  '''
  TEMPLATE VERSION
    This version follows the generalized template strictly
    Let's think about three variables
      - days: [0, n-1]
      - trading times: [0, n]
      - actions: sell or buy
  Complexity:
    Time: O(n)
    Space: O(4n)
  '''
  def maxProfit2(self, prices):
    n = len(prices)
    # the maximum length of k equals to n+1
    DP0 = [[0] * (n+1) for _ in range(n)]
    DP1 = [[0] * (n+1) for _ in range(n)]

    # initialize DP0 DP1 at k=0 and i=0
    for i in range(n):
      DP1[i][0] = float('-INF')
    for ki in range(n+1):
      DP1[0][ki] = -prices[0]

    # Loop
    for i in range(1, n):
      for k in range(1, n+1):
        DP0[i][k] = max(DP0[i-1][k], DP1[i-1][k]+prices[i])
        DP1[i][k] = max(DP1[i-1][k], DP0[i-1][k-1]-prices[i])
    
    return DP0[n-1][n]


## Run code after defining input and solver
input = [7,6,4,6,8,3]
solver = Solution().maxProfit0
print(solver(input))