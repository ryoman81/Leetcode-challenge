'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []
 
Constraints:
0 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''


class Solution:
  '''
  MY CODE VERSION
  Thought:
    The problem is very classic! And we usually have two approaches:
      1. Using hash table and convert to 2Sum problem
      2. Or using two pointers, but we still need to convert to 2Sum problem
    The first approach excess time limit O(n^2)
    The second approach is also O(n^2) I believe. But it is faster (I think the worst is O(n^2/4))
    Now the thought should combine with 167 that 
      1. sort the entire array O(nlogn)
      2. Outlayer loop over the negative numbers
      3. start two pointers at the interval of [i+1, end]
      4. search for the sum that equals to -nums[i]
  Complexity:
    Time: O(n^2)
    Space: O(1)
  '''
  def threeSum(self, nums):
    # error check for array less than three element
    if len(nums) < 3:
      return []

    # sort nums in order to work on two pointer method
    nums.sort()
    
    # loop over the non-positive numbers
    result = []
    i = 0
    while i < len(nums) and nums[i] <= 0: # we need '=' because there might be three 0s
      # for specific requirement that the result should not be duplicate
      if i > 0 and nums[i] == nums[i-1]:
        i += 1
        continue

      # then use two pointers to find the target 
      left = i + 1
      right = len(nums) - 1
      while left < right:
        sum = nums[left] + nums[right]
        if sum < -nums[i]:
          left += 1
        elif sum > -nums[i]: 
          right -= 1
        else:
          result.append([nums[i], nums[left], nums[right]])
          left += 1
          right -= 1
          # additional step to rule out the duplicate numbers
          while left < right and nums[left] == nums[left-1]:
            left += 1
          while left < right and nums[right] == nums[right+1]:
            right -= 1
      
      # move to the next non-positive number
      i += 1

    return result


## Run code after defining input and solver
input1 = [0,0,0]
solver = Solution().threeSum
print(solver(input1))