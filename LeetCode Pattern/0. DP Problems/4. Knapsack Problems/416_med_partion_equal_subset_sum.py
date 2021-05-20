'''
Given a non-empty array nums containing only positive integers, 
find if the array can be partitioned into two subsets such that 
the sum of elements in both subsets is equal.

Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 
Constraints:
1 <= nums.length <= 200
1 <= nums[i] <= 100
'''


class Solution:
  '''
  MY CODE VERSION
  Thought:
    Type: 0/1 Knapsack Problem; fulfill the knapsack (完全装满类型)
    Definition: 
      - Find N items from nums that sum up to the value of sum(nums)/2
      - In this problem, the weight equals to the value of each item
    DP template:
      - DP[j]: the best value at capacity of j (we will see that DP[j] = j or -inf)
      - Transition: DP[j] = max(DP[j], DP[j-nums[i-1]]+nums[i-1])
        -> nums array has one index lag back to DP index
        -> the weight and value is equal in this problem
      - Init: DP = -INF, DP[0] = 0
  Complexity:
    Time: O(n*sum/2)
    Space: O(sum/2)
  '''
  def canPartition0(self, nums):
    n = len(nums)
    # if the sum of all items is odd, then it can never divided into two equal half
    if sum(nums) % 2: return False

    # find the capacity of each half of the sub-array
    capacity = int (sum(nums) / 2)

    # initialize DP as 0/1 knapsack template of 完全装满类型
    DP = [float('-inf')] * (capacity+1)
    DP[0] = 0
    
    # loop over i of each number, and j of each possible capacity
    for i in range(1, n+1):
      # as 0/1 knapsack problem, the inner loop should be reverse
      for j in range(capacity, nums[i-1]-1, -1):
        # the index of nums array has one lag back
        DP[j] = max(DP[j], DP[j-nums[i-1]] + nums[i-1])
    # if DP[capacity] has a valid value, it must be capacity, otherwise -inf
    return True if DP[capacity]>0 else False

## Run code after defining input and solver
input = [1,1,1,2,3]
solver = Solution().canPartition0
print(solver(input))