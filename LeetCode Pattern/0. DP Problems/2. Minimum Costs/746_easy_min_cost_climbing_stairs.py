'''
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).
Once you pay the cost, you can either climb one or two steps. 
You need to find minimum cost to reach the top of the floor, 
and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.

Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].

Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].
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