'''
You are installing a billboard and want it to have the largest height. 
The billboard will have two steel supports, one on each side. Each steel support must be an equal height.
You are given a collection of rods that can be welded together. For example, if you have rods of 
lengths 1, 2, and 3, you can weld them together to make a support of length 6.
Return the largest possible height of your billboard installation. If you cannot support the billboard, return 0.

Example 1:
Input: rods = [1,2,3,6]
Output: 6
Explanation: We have two disjoint subsets {1,2,3} and {6}, which have the same sum = 6.

Example 2:
Input: rods = [1,2,3,4,5,6]
Output: 10
Explanation: We have two disjoint subsets {2,3,5} and {4,6}, which have the same sum = 10.

Example 3:
Input: rods = [1,2]
Output: 0
Explanation: The billboard cannot be supported, so we return 0.

Constraints:
1 <= rods.length <= 20
1 <= rods[i] <= 1000
sum(rods[i]) <= 5000
'''

import math

class Solution:
  '''
  MY CODE VERSION
  Thought:
    Type: 0/1 Knapsack Problem
    Definition: 
      - Find N items from nums that sum up to the value of sum(nums)/2
    DP template:
      - DP[j]: the maximum height of j
      - Transition: DP[j] = max(DP[j], DP[j-nums[i-1]]+nums[i-1])
      - Init: DP = -INF, DP[0] = 0
  Complexity:
    Time: O(n*sum/2)
    Space: O(sum/2)
  '''
  def tallestBillboard(self, rods):
    n = len(rods)
    cap = int(sum(rods)/2)

    DP = [0] * (cap+1)
    DP[0] = 0

    for i in range(1, n+1):
      for j in range(cap, rods[i-1]-1, -1):
        if j >= rods[i-1]:
          DP[j] = max(DP[j], DP[j-rods[i-1]]+rods[i-1])

    return DP[cap]

## Run code after defining input and solver
input = [1,2]
solver = Solution().tallestBillboard
print(solver(input))