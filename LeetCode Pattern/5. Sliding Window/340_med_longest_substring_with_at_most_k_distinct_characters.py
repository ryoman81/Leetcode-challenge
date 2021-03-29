'''
Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:
Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.

Example 2:
Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.
'''


class Solution:
  '''
  THE OPTIMAL CODE VERSION
  Improvement:
    - Use sliding window template
    - Add 'count' variable (compared to my result) to track the requirement (minimum k)
  Thought:
    - Hash table track the number of unique char within the window
    - Use count to track the number of current unique char
    - Loop over the right pointer along the string
    - Right-move left pointer if excess the k requirement
  Complexity:
    Time: O(n)
    Space: O(1)
  '''
  def lengthOfLongestSubstringKDistinctOpt(self, str, k):
    ## Check the constraint
    # Insufficient constraint information

    ## Initialize hash table to record target change
    # Hash table records the number of each char within the window
    hashTable = {}
    
    ## Initialize common variables for sliding window problem
    left = 0        # left pointer
    result = 0      # the returning result
    count = 0       # the current unique chars

    ## Loop over the main string by moving the right pointer
    for right in range(len(str)):
      ## Update the right most char in hash table
      if str[right] in hashTable:
        hashTable[str[right]] += 1
      else:
        hashTable[str[right]] = 1
        count += 1
      ## Check the count condition
      # if the number of different char larger than k
      while count > k:
        hashTable[str[left]] -= 1
        ## usually update left and count at this place  
        if hashTable[str[left]] <= 0:
          count -= 1
        left += 1
      ## Update result after while loop or within while loop
      result = max(result, right - left + 1)

    ## return result        
    return result

  '''
  MY CODE VERSION
  Thought:
    - Same as the optimal code
  Complexity:
    Time: O(n)
    Space: O(1)
  '''
  def lengthOfLongestSubstringKDistinct(self, str, k):
    hashTable = {}
    left = 0
    result = 0
    for right in range(len(str)):
      if str[right] not in hashTable:
        hashTable[str[right]] = 1
      else:
        hashTable[str[right]] += 1
      while len(hashTable) > k:
        hashTable[str[left]] -= 1
        if hashTable[str[left]] == 0:
          del hashTable[str[left]]
        left += 1
      result = max(result, right-left+1)
    return result


## Run code after defining input and solver
input1 = 'eceba'
input2 = 2
solver = Solution().lengthOfLongestSubstringKDistinctOpt
print(solver(input1, input2))