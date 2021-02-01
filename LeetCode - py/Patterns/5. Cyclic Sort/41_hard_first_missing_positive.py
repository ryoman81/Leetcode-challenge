'''
Given an unsorted integer array nums, find the smallest missing positive integer.

Example 1:
Input: nums = [1,2,0]
Output: 3

Example 2:
Input: nums = [3,4,-1,1]
Output: 2

Example 3:
Input: nums = [7,8,9,11,12]
Output: 1

Constraints:
0 <= nums.length <= 300
-231 <= nums[i] <= 231 - 1
'''


class Solution:
  '''
  THE OPTIMAL CODE VERSION
  Thought:
    Using cyclic sort we want to put element in its indexing of value
    The we will have several situations in this problem
      1. the value is larger than the length
      2. the value is negative
      3. the value is the same as the value in target position
    If above, we don't need to swap nums[i] and nums[crr-1]. just make them placed in the hole
    Finally loop over the index and check if nums[i] = i+1
      - Find the first place where a wrong number sit in that hole
      - Or output the length+1 (e.g. [4,2,3,1] we should output 5 as the first positive)

  Complexity:
    Time: O(n)
    Space: O(1)
  '''
  def firstMissingPositiveOpt(self, nums):
    i = 0
    while i < len(nums):
      crr = nums[i]
      # We should put crr value at the index of crr-1!
      if crr <= len(nums) and crr > 0 and crr != nums[crr-1]:
        nums[i], nums[crr-1] = nums[crr-1], nums[i]
      else:
        i += 1
    
    for i in range(len(nums)):
      if nums[i] != i+1:
        return i+1

    return len(nums)+1


## Run code after defining input and solver
input = [-1,-1,-1,-1]
solver = Solution().firstMissingPositiveOpt
print(solver(input))