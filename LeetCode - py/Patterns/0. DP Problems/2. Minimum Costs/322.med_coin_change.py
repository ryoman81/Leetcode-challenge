'''
You are given an integer array coins representing coins of different denominations 
and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0

Example 4:
Input: coins = [1], amount = 1
Output: 1

Example 5:
Input: coins = [1], amount = 2
Output: 2
 
Constraints:
1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
'''


class Solution:
  '''
  MY CODE VERSION
  Thought:
    Dynamic Programming template:
      State: DP[n] - the minimum cost when stepping to nth stair
      Transition: DP[i] = min(DP[i-1], DP[i-2]) + cost[i-1]
        ** the index of cost is due to one shift of indexing between cost and DP
      Initial states: DP[0], DP[1]
  Complexity:
    Time: O(n)
    Space: O(n) - space optimization available
  '''
  def minCostClimbingStairs(self, cost):
    # Create DP state with 1 x (n+1) because we include stair 0
    n = len(cost)
    DP = [0] * (n+1)

    # Initialize DP at 0 and 1 positions
    DP[1] = cost[0]

    # Construct DP
    for i in range(2, n+1):
      DP[i] = min(DP[i-1], DP[i-2]) + cost[i-1]

    return min(DP[n], DP[n-1])


## Run code after defining input and solver
input = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
solver = Solution().minCostClimbingStairs
print(solver(input))