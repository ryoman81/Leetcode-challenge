'''
Given two strings s and t, return the minimum window in s which will contain all the characters in t. 
If there is no such window in s that covers all characters in t, return the empty string "".
Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

Example 2:
Input: s = "a", t = "a"
Output: "a"
 
Constraints:
1 <= s.length, t.length <= 105
s and t consist of English letters.

Follow up: Could you find an algorithm that runs in O(n) time?
'''


class Solution:
  '''
  THE OPTIMAL CODE VERSION
  Improvement:
    - Follow the template (see ## commends)
    - Keep the time complexity as O(n)
  Thought:
    1. Keep a hash table to track the number of each char in target string
    2. Use 'count' to track if all chars are within the window
    3. Loop over string using right pointer and right-move left pointer based on condition
    4. Update 'result' in the checking step, need additional 'minLen' to do the comparison
  Complexity:
    Time: O(n)  - Single loop over string
    Space: O(1) - Hash table size
  '''
  def minWindowOpt(self, s: str, t: str) -> str:
    ## Check the constraint
    if len(t) > len(s): 
      return ""

    ## Initialize hash table to record target change
    # In this problem, hash table tracks the number of each char in target string
    # since char in target string may duplicate
    hashTable = {}
    for char in t:
      if char in hashTable:
        hashTable[char] += 1
      else:
        hashTable[char] = 1
    
    ## Initialize common variables for sliding window problem
    left = 0        # left pointer
    result = ""     # the returning result
    count = 0       # the number of target char found in main string
    minLen = len(s) # a record of minimum length of result

    ## Loop over the main string by moving the right pointer
    for right in range(len(s)):
      ## Update the right most char in hash table
      if s[right] in hashTable:
        hashTable[s[right]] -= 1
        ## count up if eligibly capture a target char
        if hashTable[s[right]] >= 0:
          count += 1

      ## Check the count condition and update result
      ## Usually update result at this place
      # This is a positive check once the requirement meet 
      while count == len(t):
        if (minLen >= right - left + 1):
          minLen = right - left + 1
          result = s[left:right+1]
        ## update the left pointer if condition meet
        ## usually update left and count at this place  
        if s[left] in hashTable:
          hashTable[s[left]] += 1
          if hashTable[s[left]] > 0:
            count -= 1
        left += 1

    ## return result        
    return result

  '''
  MY CODE VERSION
  Thought:
    - Follow the sliding window template using left and right pointers
    - Loop over right pointer
    - Update left if condition meet
    - Key is define hashTable to count repeating times for each char in t
  Complexity:
    Time: O(n)
    Space: O(1)
  '''
  def minWindow(self, s: str, t: str) -> str:
    hashTable = {}
    result = ''
    count = 0
    left = 0
    minLen = len(s)

    # Initialize hashTable
    for char in t:
      if char in hashTable:
        hashTable[char] += 1
      else:
        hashTable[char] = 1
    
    # Loop over string by moving right pointer
    for right in range(len(s)):
      # update hashTable
      # if the incoming char in hashTable
      if s[right] in hashTable:
        hashTable[s[right]] -= 1
        # if the incoming char count up position in t string
        if hashTable[s[right]] >= 0:
          count += 1
    
      # Update result and move left pointer
      while count == len(t):
        # record result if meet requirement
        if minLen > right - left + 1:
          minLen = right - left + 1
          result = s[left:right+1]
        # reduce the count of char in the left pointer
        if s[left] in hashTable:
          hashTable[s[left]] += 1
          if hashTable[s[left]] > 0:
            count -= 1
        # for any case increase left pointer
        left += 1
    ## return result 
    return result


## Run code after defining input and solver
input1 = 'ADOBECODEBANC'
input2 = 'ABC'
solver = Solution().minWindowOpt
print(solver(input1, input2))