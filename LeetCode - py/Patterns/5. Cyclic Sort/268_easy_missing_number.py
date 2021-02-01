'''
Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.
Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Example 2:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

Example 4:
Input: nums = [0]
Output: 1
Explanation: n = 1 since there is 1 number, so all numbers are in the range [0,1]. 1 is the missing number in the range since it does not appear in nums.

Constraints:
n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
All the numbers of nums are unique.
'''


class Solution:
  '''
  THE OPTIMAL CODE VERSION - MATH METHOD
  Improvement:
    The best method of this problem is not cyclic sort
    Thinking in mathematical theorem behind can be much easier
  Thought:
    - summation from 0 to n is n(n+1)/2
    - the missing number can be found easily by substracting each item and see the remaining value
  Complexity:
    Time: O(n)
    Space: O(1)
  '''
  def missingNumberMath(self, nums):
    n = len(nums)
    sum = n * (n+1) / 2
    for item in nums:
      sum = sum - item
    return int(sum)

  '''
  THE OPTIMAL CODE VERSION - Bit Manipulation
  Improvement:
    Another optimal method is also not cyclic sort
    This is another important category - Bit Manipulation
    The key is using XOR where a^a=0 a^0=a a^b^b=a
  Thought:
    - We need to XOR all element of [0,1,...,n] and given array
    - The remaining result is the missing number which cannot be XOR
  Complexity:
    Time: O(n)
    Space: O(1)
  '''
  def missingNumberBitM(self, nums):
    x = 0
    for i in range(1, len(nums)):
      x = x ^ i ^ nums[i]
    return x
    
  '''
  MY CODE VERSION
  Thought:
    We can also use cyclic sort (as this topic) to put the current item in its index place
    Be careful about the indexing of the last element
      - for example, nums come from [0, 10]
      - missing one value, hence, the length is 10
      - but we cannot index nums[10] due to indexing range limit
    Once cyclic sorted, check if nums[i] == i
      - if not, return this location i as the missing value
      - if all passed, the last item is missing return length
  Complexity:
    Time: O(n)
    Space: O(1)
  '''
  def missingNumber(self, nums):
    i = 0
    while i < len(nums):
      crr = nums[i]
      # we don't move the number n because the index n outside the range
      # after while-loop, the n will be placed on the position of missing value
      if crr < len(nums) and crr != nums[crr]:
        nums[i], nums[crr] = nums[crr], nums[i]
      else:
        i += 1
    # check if item i at the same index of i    
    for i in range(len(nums)):
      if nums[i] != i:
        return i
    # if all value at its indexing location, the last item is missing
    return len(nums)


## Run code after defining input and solver
input = [0,6,4,2,3,5,7,9,1]
solver = Solution().missingNumber
print(solver(input))