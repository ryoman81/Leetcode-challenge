'''
You are given an integer array nums sorted in ascending order (not necessarily distinct values), and an integer target.
Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,4,4,5,6,6,7] might become [4,5,6,6,7,0,1,2,4,4]).
If target is found in the array return its index, otherwise, return -1.

Example 1:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
 
Constraints:
1 <= nums.length <= 5000
-104 <= nums[i] <= 104
nums is guaranteed to be rotated at some pivot.
-104 <= target <= 104
'''


class Solution:
  '''
  THE OPTIMAL CODE VERSION
  Improvement:
    1.
  Thought:
    1.  
  Complexity:
    Time: O()
    Space: O()
  '''
  def functionOpt(self):
    return 0

  '''
  MY CODE VERSION
  Thought:
    1. 
  Complexity:
    Time: O()
    Space: O()
  '''
  def search(self, nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
      mid = (left + right) // 2
      if nums[mid] == target:
        return True

      # right sorted
      if nums[mid] < nums[right]:
        if nums[mid] < target and nums[right] >= target:
          left = mid + 1
        else:
          right = mid -1
      # left sorted
      elif nums[mid] > nums[right]:
        if nums[left] <= target and nums[mid] > target:
          right = mid - 1
        else:
          left = mid + 1
      # else we meet a situation that rotated portion covers left and right part
      else:
        right -= 1
      
    return False


## Run code after defining input and solver
input1 = [2,5,6,0,0,1,2]
input2 = 3
solver = Solution().search
print(solver(input1, input2))