'''
Given an array of integers numbers that is already sorted in ascending order, 
find two numbers such that they add up to a specific target number.
Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, 
where 1 <= answer[0] < answer[1] <= numbers.length.
You may assume that each input would have exactly one solution and you may not use the same element twice.

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
 
Constraints:
2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in increasing order.
-1000 <= target <= 1000
Only one valid answer exists.
'''


class Solution:
  '''
  MY CODE VERSION
  Thought:
    The problem is easy as the Number 1 problem - two sum. 
    We can use the same method that using a hash table to record the number we met.
    But since the array is sorted, and we are in the topic of two pointers, let's solve it using this technique.
    - define two pointers at the head and tail
    - let both move to the center and check if sum is target
    - conditionally move left or right pointer based on the result
  Complexity:
    Time: O(n)
    Space: O(1)
  '''
  def twoSum(self, numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
      sum = numbers[left] + numbers[right]
      if sum == target:
        return [left+1, right+1]
      elif sum < target:
        left += 1
      else:
        right -= 1

    return 0


## Run code after defining input and solver
input1 = [2,7,11,15]
input2 = 9
solver = Solution().twoSum
print(solver(input1, input2))