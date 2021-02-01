'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3

Example 3:
Input: nums = [1,1]
Output: 1

Example 4:
Input: nums = [1,1,2]
Output: 1
 
Constraints:
2 <= n <= 3 * 104
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.

Follow up:
How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem without modifying the array nums?
Can you solve the problem using only constant, O(1) extra space?
Can you solve the problem with runtime complexity less than O(n2)?
'''


class Solution:
  '''
  THE OPTIMAL CODE VERSION
  Improvement:
    If using constant space with O(n) time expense, there is cyclic sort (as we topiced it!!) 
  Thought:
    - loop over the numbers and put it into the corresponding indexing place
    - if special condition meet: the current value is the same as in the destination place
    - we return this special
  Complexity:
    Time: O(n)
    Space: O(1)
  '''
  def findDuplicateOpt(self, nums):
    i = 0
    while i < len(nums):
      crr = nums[i]

      if crr == nums[crr-1]:
        if i == crr-1:
          i += 1
        else:
          return crr
      else:
        nums[i], nums[crr-1] = nums[crr-1], nums[i]

    return False

  '''
  MY CODE VERSION
  Thought:
    This is a very brief method came up on everybody's mind
    Use a hashmap and see if the current item is in the map
      - if not, create one
      - if yes, the duplicate happens, and return it
  Complexity:
    Time: O(n)
    Space: O(n)
  '''
  def findDuplicate(self, nums):
    hashTable = {}
    for item in nums:
      if item not in hashTable:
        hashTable[item] = 1
      else:
        return item
    return False


## Run code after defining input and solver
input = [1,1]
solver = Solution().findDuplicateOpt
print(solver(input))