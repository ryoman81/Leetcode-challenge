'''
Given n pairs of parentheses, write a function to generate 
all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

Constraints:
1 <= n <= 8
'''


class Solution:
  '''
  OPTIMAL CODE VERSION
  Thought:
    My solution is more time-complex since we will brute force all possible combination
    Pruning is performed in this answer, that we use left and right counters to track the total number of '(' ')'
      - We still follow backtracking template, but with pruning before to the next
      - if left > n: there is no more room for right ')'
      - if right > left: the parentheses cannot be even
  Complexity:
    Time: O()
    Space: O()
  '''
  def generateParenthesis(self, n):
    result = []
    path = []

    def backtracking (left, right):
      # base case if meet n length
      if len(path) == n*2:
        result.append(''.join(path))
        return

      if left < n:
        path.append('(')
        backtracking(left+1, right)
        path.pop()
      if right < left:
        path.append(')')
        backtracking(left, right+1)
        path.pop()

    backtracking(0, 0)
    return result


  '''
  MY CODE VERSION
  Thought:
    
  Complexity:
    Time: O()
    Space: O()
  '''
  def generateParenthesis2(self, n):
    result = []
    path = []

    def backtracking ():
      # base case if meet n lengh and valid
      if len(path) == n*2:
        if self.validate(path):
          result.append(''.join(path))
        return

      for i in ['(', ')']:
        path.append(i)
        backtracking ()
        path.pop()
        
    backtracking()
    return result

  # this is a helper function to validate if path is validate
  # similar as question 20 where we used a stack to check path validation
  def validate(self, path):
    stack = [path[0]]
    for i in range(1, len(path)):
      stack.append(path[i])
      if len(stack) < 2: continue
      left = stack[-2]
      right = stack[-1]
      if (left == '(' and right == ')'):
        stack.pop()
        stack.pop()

    if not stack:
      return True
    else:
      return False

## Run code after defining input and solver
input = 3
solver = Solution().generateParenthesis
print(solver(input))