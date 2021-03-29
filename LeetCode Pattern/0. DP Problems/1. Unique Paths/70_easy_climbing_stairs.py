'''
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. 
In how many distinct ways can you climb to the top? 

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 
Constraints:
1 <= n <= 45
'''


class Solution:
  '''
  SAPCE OPTIMIZED VERSION
  Thought:
    Space optimization
      - first = DP[n-1]
      - second = DP[n-2]
  Complexity:
    Time: O(n)
    Space: O(1)
  '''
  def climbStairs(self, n):
    # Check initial cases to which DP cannot cover
    if n <= 2:
      return n

    # Define the initial state
    second = 1
    first = 2

    # bottom-up to construct DP
    for i in range(2, n):
      crr = first + second
      first, second = crr, first
      
    return first


  '''
  MY CODE VERSION
  Thought:
    Dynamic Programming template:
      State: DP[n] - number of ways ways to climb to (n+1)th stair
      Transition: DP[n] = DP[n-1] + DP[n-2]
      Initial states: DP[0] (climbing to 1rt stair); DP[1] (climbing to 2nd stair)
  Complexity:
    Time: O(n)
    Space: O(n) - space optimization available
  '''
  def climbStairs2(self, n):
    # Check initial cases to which DP cannot cover
    if n <= 2:
      return n

    # Define state DP[] = [0,0,...,0]
    DP = [0] * n
    
    # Initialize DP
    DP[0] = 1
    DP[1] = 2

    # bottom-up to construct DP
    for i in range(2, n):
      DP[i] = DP[i-1] + DP[i-2]
      
    return DP[n-1]


## Run code after defining input and solver
input = 5
solver = Solution().climbStairs
print(solver(input))