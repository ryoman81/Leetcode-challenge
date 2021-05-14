'''
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, the only constraint stopping you 
from robbing each of them is that adjacent houses have security systems connected 
and it will automatically contact the police if two adjacent houses were 
broken into on the same night.
Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police. 

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 
Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 400
'''


class Solution:
  '''
  MY CODE VERSION
  Dynamic Programming template:
    State DP[n] - the maximum amount we can rob at nth house
    Transition - DP[n] = max(max(DP[0...n-2])+nums[n-1], DP[n-1])
    Initial state: DP[0]=0 DP[1]=nums[0]
  Complexity:
    Time: O(n)
    Space: O(n)
  '''
  def rob(self, nums):
    n = len(nums)

    # create DP array
    DP = [0] * (n+1)
    # initialize DP
    DP[0] = 0
    DP[1] = nums[0]

    # loop over to create DP
    for i in range(2, n+1):
      left = max(DP[:i-1]) + nums[i-1]
      right = DP[i-1]
      DP[i] = max(left, right)

    return DP[n]


## Run code after defining input and solver
input = [2,7,9,3,1]
solver = Solution().rob
print(solver(input))