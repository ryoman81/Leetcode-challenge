'''
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
For example, the array nums = [0,1,2,4,5,6,7] might become:
[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Given the sorted rotated array nums, return the minimum element of this array.

Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Example 3:
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 

Constraints:
n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.
'''


class Solution:
  '''
  THE OPTIMAL CODE VERSION
  Thought:
    This is the combination of 33 and 35
      - we want to search in a rotated sorted array
      - we also want to exhaust the while loop to find the minimum
      - the minimum can exist in BOTH UNSORTED PART or MID point itself
    As the template, here we use RIGHT to compare with mid by < (not <=, see explanation 1)
    
    If we stick on the template, there must be some exceptions...

  Complexity:
    Time: O(logn)
    Space: O(1)
  '''
  def findMin(self, nums):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
      mid = (left + right) // 2

      if left == right: 
        break

      # the right part is sorted, the minimum could be either 
      # !!!!!!!!!! on the left part or the mid point itself !!!!!!!!!!!
      if  nums[mid] < nums[right]:
        right = mid   # we have to include mid point itself when moving right pointer
                      # which means we can never use left<=right as while-loop condition (otherwise infinite loop)
      else:
        left = mid + 1

    return nums[left]


## Run code after defining input and solver
input = [0,1,2,4,5,6,7]
solver = Solution().findMin
print(solver(input))