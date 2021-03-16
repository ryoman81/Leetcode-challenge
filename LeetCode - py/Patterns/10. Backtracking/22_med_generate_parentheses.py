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
    Template:
      - State variable: 
        1. left: a counter of total number of '('
        2. right: a counter of total number of ')'
      - State: path[] - record current valid result along recursion
      - Choices: left or right parenthesis ['(', ')']
      - Pruning:
        1. if left > n: there is no more room for right ')' (因为每一个左括号都要配一个右括号嘛!)
        2. if right > left: the parentheses cannot be even
  Complexity:
    ref: https://leetcode-cn.com/problems/generate-parentheses/solution/gua-hao-sheng-cheng-by-leetcode-solution/
    Time: O(4^n / sqrt(n))  - 什么鬼, 卡特兰数, 渐近界定
    Space: O(n)
  '''
  def generateParenthesis(self, n):
    result = []
    path = []

    def backtracking (left, right):
      # base case if meet n length
      if len(path) == n*2:
        result.append(''.join(path))
        return

      # search solution space of ['(',')']
      # prune 1
      if left < n:
        path.append('(')
        backtracking(left+1, right)
        path.pop()
      # prune 2
      if right < left:
        path.append(')')
        backtracking(left, right+1)
        path.pop()
      
    backtracking(0, 0)
    return result


  '''
  MY CODE VERSION
  Thought:
    This is my original thought but it is less backtracking sense
    问题出在, 我们在穷举所有可能, 直到base case的时候才去判断当前这个路径是否成立.
    对比更加backtracking的思路, 在到达base case的时候, 我们通过剪枝保证了当前path是有效的.
  Complexity:
    Time: O(n * 2^2n)   - 官方这么写的.. 好复杂
    Space: O(n * 2^2n)
  '''
  def generateParenthesis2(self, n):
    result = []
    path = []

    def backtracking ():
      # base case if meet n length
      if len(path) == n*2:
        # we validate if current path is valid via a helping function
        if self.validate(path):
          # if valid, we convert array to a string and append it
          result.append(''.join(path))
        return
      # search solution space
      for i in ['(', ')']:
        # set state
        path.append(i)
        # do backtracking
        backtracking ()
        # reset state
        path.pop()
        
    backtracking()
    return result

  # this is a helper function to validate if path is validate
  # similar to question 20 where we used a stack to check path validation
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