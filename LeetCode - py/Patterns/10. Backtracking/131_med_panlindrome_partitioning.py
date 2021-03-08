'''
Given a string s, partition s such that every substring of the partition is a palindrome. 
Return all possible palindrome partitioning of s.
A palindrome string is a string that reads the same backward as forward.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]
 
Constraints:
1 <= s.length <= 16
s contains only lowercase English letters.
'''


class Solution:
  '''
  MY CODE VERSION
  Thought:
     
     The efficiency can be improved using DP
  Complexity:
    Time: O()
    Space: O()
  '''
  def partition(self, s):
    result = []
    path = []

    def backtracking(start):
      if start == len(s):
        result.append(path[:])

      for i in range(start, len(s)):
        substr = s[start:i+1]
        # prune if the current substr is not validate
        if not self.validate(substr):
          continue
        path.append(substr)
        backtracking(i+1)
        path.pop()
        
    backtracking(0)
    return result

  # A helper function (actually my AMAZON interview question!!!) to check if palindrome
  # two pointer solution (no need to check if even or odd)
  # simular to question 9
  def validate(self, str):
    left = 0
    right = len(str) - 1
    while left < right:
      if str[left] != str[right]:
        return False
      left += 1
      right -= 1
    return True

## Run code after defining input and solver
input = "aab"
solver = Solution().partition
print(solver(input))