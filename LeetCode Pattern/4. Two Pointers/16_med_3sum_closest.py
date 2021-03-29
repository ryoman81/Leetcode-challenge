'''
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. 
Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Constraints:
3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4
'''


class Solution:
  '''
  MY CODE VERSION
  Thought:
    The problem looks like 15.3sum, but less troublesome for ruling out duplication.
      - We still need to sort this array in order to use two sum
      - We need to update a result if its difference with target is smaller
      - Finally update left or right pointer like in 2Sum problem
  Complexity:
    Time: O(n^2)
    Space: O(1)
  '''
  def threeSumClosest(self, nums, target):
    nums.sort()

    result = nums[0] + nums[1] + nums[2]
    diff = abs(result - target)

    for i in range(0, len(nums)-2):
      left = i + 1
      right = len(nums) - 1

      while left < right:
        sum = nums[i] + nums[left] + nums[right]

        # this is the special step for this question
        # we maintain a diff var to track on the closest distance
        # if the current difference is smaller we update it
        if abs(sum - target) < diff:
          diff = abs(sum - target)
          result = sum

        # and here we do a normal 2sum using two pointers
        if sum == target:
          return target
        elif sum < target:
          left += 1
        else:
          right -= 1

    return result


## Run code after defining input and solver
input1 = [-1,2,1,-4]
input2 = 1
solver = Solution().threeSumClosest
print(solver(input1,input2))