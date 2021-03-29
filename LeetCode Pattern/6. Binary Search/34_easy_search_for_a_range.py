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
  MY CODE VERSION
  Thought:
    The key to achieve O(logn) is using binary search TWICE
      - find the left boundary by moving right ALL THE WAY down until meet left
      - find the right boundary by moving left ALL THE WAY up until meet right
  Complexity:
    Time: O(logn)
    Space: O(1)
  Improvement:
    These two while loops can be combined together with more conditioning strategies
  '''
  def searchRange(self, nums, target):
    result = [-1, -1]
    left = 0
    right = len(nums) - 1

    # The first search of start point
    # the while loop will go to the end when right = left - 1
    while (left <= right):
      mid = (left + right) // 2
      # lift left up up up to hit the left boundary
      if nums[mid] < target:
        left = mid + 1
      # move right down down down even right == target since we only want to find left boundary
      else:
        right = mid - 1
    # when out the first while loop, it indicate that right = left - 1
    # we use the current left to index the left boundary

    # to avoid failed scenario that left and right merged but no target meet
    # we should also exclude one situation that left went up all the way to the right+1, at which moment that num[left] would exist
    if left == len(nums) or nums[left] != target:
      return [-1,-1]
    else:
      result[0] = left

    left = right            # update left to the beginning of new search region
    right = len(nums) - 1   # also reset right to nums boundary
    # the similar while loop until left catch up the right
    while (left <= right):
      mid = (left + right) // 2
      if nums[mid] > target:
        right = mid - 1
      else:
        left = mid + 1

    if nums[right] != target:
      return [-1,-1]
    else:
      result[1] = right
    
    return result


## Run code after defining input and solver
input1 = [5,7,7,8,8,10]
input2 = 8
solver = Solution().searchRange
print(solver(input1, input2))