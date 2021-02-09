'''
Given an array nums and a value val, remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2]
Explanation: Your function should return length = 2, with the first two elements of nums being 2.
It doesn't matter what you leave beyond the returned length. For example if you return 2 with nums = [2,2,3,3] or nums = [2,2,0,0], your answer will be accepted.

Example 2:
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3]
Explanation: Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4. 
Note that the order of those five elements can be arbitrary. It doesn't matter what values are set beyond the returned length.
 
Constraints:
0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100
'''

class Solution:
  '''
  FAST SLOW POINTER VERSION
  Thought:
    This first solution use fast slow pointers (the next one uses left right pointers)
      - We iterate fast pointer to the end of array
      - 

  Complexity:
    Time: O(n)
    Space: O(1)
  '''
  def removeElement(self, nums, val):
    fast = 0
    slow = 0
    
    while fast < len(nums):
      if nums[fast] != val:
        nums[slow], nums[fast] = nums[fast], nums[slow]
        slow += 1
      fast += 1
    
    return slow

  '''
  LEFT RIGHT POINTER VERSION
  Thought:
    In the idea of left right pointers, we want to move all target value to the end of array
    And we only want to return a length that covers the front part that contains no target value
      - first we initiate left and right pointers
      - loop over and check if left meet a target val
      - if met target value swap it with value in right pointer
      - and move back right pointer
    Final we update whole array in-place and we return right pointer (+1) to denotes the length
  Complexity:
    Time: O(n)
    Space: O(1)
  '''
  def removeElement2(self, nums, val):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
      if nums[left] == val:
        nums[left], nums[right] = nums[right], nums[left]
        right -= 1
      else:
        left += 1
    
    return right+1



## Run code after defining input and solver
input1 = [0,1,2,2,3,0,4,2]
input2 = 2
solver = Solution().removeElement
print(solver(input1, input2))