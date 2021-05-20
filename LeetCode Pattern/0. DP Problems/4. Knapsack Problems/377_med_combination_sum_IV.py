'''
Given an array of distinct integers nums and a target integer target, 
return the number of possible combinations that add up to target.
The answer is guaranteed to fit in a 32-bit integer.

Example 1:
Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.

Example 2:
Input: nums = [9], target = 3
Output: 0
 
Constraints:
1 <= nums.length <= 200
1 <= nums[i] <= 1000
All the elements of nums are unique.
1 <= target <= 1000
'''


class Solution:
  '''
  MY CODE VERSION
  Thought:
    
  Complexity:
    
  '''
  def combinationSum4(self, nums, target):
    n = len(nums)
    
    DP = [0] * (target+1)
    DP[0] = 1

    for i in range(1, target+1):
      for j in range(1, n+1):
        if i >= nums[j-1]:
          DP[i] = DP[i] + DP[i-nums[j-1]]

    return DP[target]


## Run code after defining input and solver
input1 = [1,2,3]
input2 = 4
solver = Solution().combinationSum4
print(solver(input1, input2))