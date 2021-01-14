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
    MY CODE VERSION
    Thought:
      1. 
    Complexity:
      Time: O()
      Space: O()
    '''
    def minWindow(self, s: str, t: str) -> str:
      hashTable = {}
      result = ''
      
      return result

    '''
    THE OPTIMAL CODE VERSION
    Improvement:
      1.
    Thought:
      1.  
    Complexity:
      Time: O(n)
      Space: O(m)
    '''
    def minWindowOpt(self, s: str, t: str) -> str:
      # contraint check if t > s
      if len(t) > len(s): return ""

      # create hash table to count the number of each char in target
      hashTable = {}
      for char in t:
        if char in hashTable:
          hashTable[char] += 1
        else:
          hashTable[char] = 1
      
      # initial the template variables
      left = 0        # left pointer
      count = 0       # the number of target char found in main string
      result = ""     # the returning result
      minLen = len(s) # a record of minimum length of result

      # right pointer loop over the main string
      for right in range(len(s)):
        if s[right] in hashTable:
          hashTable[s[right]] -= 1
          if hashTable[s[right]] >= 0:
            count += 1
        
        while count == len(t):
          if (minLen >= right - left + 1):
            minLen = right - left + 1
            result = s[left:right+1]
            
          if s[left] in hashTable:
            hashTable[s[left]] += 1
            if hashTable[s[left]] > 0:
              count -= 1
          left += 1      
      return result


## Run code after defining input and solver
input1 = 'ADOBECODEBANC'
input2 = 'ABCD'
solver = Solution().minWindowOpt
print(solver(input1, input2))