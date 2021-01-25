'''
Given an array of integers nums sorted in ascending order, 
find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]

Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
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
    The key to achieve O(logn) is using binary search TWICE
  Complexity:
    Time: O()
    Space: O()
  '''
  def searchRange(self, nums, target):
    # The first search of start point
    result = [-1, -1]
    left = 0
    right = len(nums) - 1

    while (left <= right):
      mid = (left + right) // 2
      if nums[mid] < target:
        left = mid + 1
      else:
        right = mid - 1
    right += 1

    if right == len(nums) or nums[right] != target:
      return [-1,-1]
    else:
      result[0] = right

    left = right
    right = len(nums) - 1
    while (left <= right):
      mid = (left + right) // 2
      if nums[mid] > target:
        right = mid - 1
      else:
        left = mid + 1
    left -= 1

    if nums[left] != target:
      return [-1,-1]
    else:
      result[1] = left
    
    return result


## Run code after defining input and solver
input1 = [5,7,7,8,8,10]
input2 = 11
solver = Solution().searchRange
print(solver(input1, input2))