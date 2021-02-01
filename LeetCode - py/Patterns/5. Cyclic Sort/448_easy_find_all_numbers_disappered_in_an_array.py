'''
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements of [1, n] inclusive that do not appear in this array.
Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:
Input: [4,3,2,7,8,2,3,1]
Output:[5,6]
'''


class Solution:
  '''
  THE OPTIMAL CODE VERSION
  Improvement:
    For saving the memory space, we should do in-place counting on the nums array, where cyclic sort is in stage!!
  Thought:
    - put crr=num[i] to nums[crr-1] as the convention of array starting point by 1
    - if duplicate then do not swap (don't worry, somebody else will take in this place)
  Complexity:
    Time: O(n)
    Space: O(1)
  '''
  def findDisappearedNumbersOpt(self, nums):
    result = []
    i = 0
    while i < len(nums):
      crr = nums[i]
      # swap if the current number is not duplicated at the destination
      if crr != nums[crr-1]:
        nums[i], nums[crr-1] = nums[crr-1], nums[i]
      else:
        i += 1

    for i in range(len(nums)):
      if nums[i] != i+1:
        result.append(i+1)

    return result

  '''
  MY CODE VERSION
  Thought:
    1. Similar to 287 that we can use HashTable to count the frequency of each number shows
    2. The size of the array so we can infer which numbers (keys) should have existed in the hashTable
    3. Loop over the hash table and check the key if exists. If not, add to result list
  Complexity:
    Time: O(n)
    Space: O(n)
  '''
  def findDisappearedNumbers(self, nums):
    hashTable = {}
    result = []
    # loop over the array and count to hash table
    for item in nums:
      if item not in hashTable:
        hashTable[item] = 1
      else:
        hashTable[item] += 1
    # loop over all possible numbers given in the problem
    # and check if any missing 
    for i in range(1, len(nums)+1):
      if i not in hashTable:
        result.append(i)
    # return result
    return result


## Run code after defining input and solver
input = [4,3,2,7,8,2,3,1]
solver = Solution().findDisappearedNumbersOpt
print(solver(input))