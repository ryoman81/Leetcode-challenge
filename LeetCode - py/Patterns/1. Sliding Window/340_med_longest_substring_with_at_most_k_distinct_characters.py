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
    MY CODE VERSION
    Thought:
      1. 
    Complexity:
      Time: O()
      Space: O()
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

    '''
    THE OPTIMAL CODE VERSION
    Improvement:
      1.
    Thought:
      1.  
    Complexity:
      Time: O()
      Space: O()
    '''
    def lengthOfLongestSubstringKDistinctOpt(self, str, k):
      return 0


## Run code after defining input and solver
input1 = 'aaabbbcaaaa'
input2 = 3
solver = Solution().lengthOfLongestSubstringKDistinct
print(solver(input1, input2))