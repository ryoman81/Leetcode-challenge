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
    1. 
  Complexity:
    Time: O()
    Space: O()
  '''
  def canPartition(self, nums):
    n = len(nums)
    capacity = sum(nums) / 2

    DP = [[0] * (capacity+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
      for j in range(1, capacity+1):
        DP[i][j] = max(DP[i-1][j], DP[i-1][j - nums[i]] + nums[i])



    return False


## Run code after defining input and solver
input = [1,5,11,5]
solver = Solution().canPartition
print(solver(input))