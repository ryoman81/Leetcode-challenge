'''
You are given an integer array prices where prices[i] is 
the price of a given stock on the ith day, and an integer k.
Find the maximum profit you can achieve. You may complete at most k transactions.
Note: You may not engage in multiple transactions simultaneously 
(i.e., you must sell the stock before you buy again).

Example 1:
Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
E
xample 2:
Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
 
Constraints:

0 <= k <= 100
0 <= prices.length <= 1000
0 <= prices[i] <= 1000
'''


class Solution:
  '''
  MY CODE VERSION
    This problem is a generalization of all stock buying and selling problem
    Answer refer to the introduction
  Complexity:
    Time: O(nK)
    Space: O(nK)
  '''
  def maxProfit(self, k, prices):
    # since length of prices could be 0, avoid boundary condition
    n = len(prices)
    if n <= 1: return 0

    # create all zero DP of 3D matrix of n*(k+1)
    DP0 = [[0] * (k+1) for _ in range(n)]
    DP1 = [[0] * (k+1) for _ in range(n)]

    # initialize DP at k=0
    for i in range(n):
      DP1[i][0] = float('-inf')
    # initialize DP at i=0
    for ki in range(k+1):
      DP1[0][ki] = -prices[0]

    # loop over i k and DP1 DP2
    for i in range(1, n):
      for ki in range(1, k+1):
        DP0[i][ki] = max(DP0[i-1][ki], DP1[i-1][ki]+prices[i])
        DP1[i][ki] = max(DP1[i-1][ki], DP0[i-1][ki-1]-prices[i])
    
    # return value at n-1th day with max K
    return DP0[n-1][k]

## Run code after defining input and solver
input1 = 1 
input2 = [3,2,6,5,0,3]
solver = Solution().maxProfit
print(solver(input1, input2))