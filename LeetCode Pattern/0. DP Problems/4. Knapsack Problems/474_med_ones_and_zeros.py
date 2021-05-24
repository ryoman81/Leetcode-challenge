'''
You are given an array of binary strings strs and two integers m and n.
Return the size of the largest subset of strs such that there are 
at most m 0's and n 1's in the subset.
A set x is a subset of a set y if all elements of x are also elements of y.

Example 1:
Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
{"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.

Example 2:
Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: The largest subset is {"0", "1"}, so the answer is 2.
 
Constraints:
1 <= strs.length <= 600
1 <= strs[i].length <= 100
strs[i] consists only of digits '0' and '1'.
1 <= m, n <= 100
'''


class Solution:
  '''
  MY CODE VERSION
  Problem Definition:
    该题是唯一一道二维的0/1背包问题. 每一个item有两种重量, 0的个数和1的个数 (-_-)
    因此背包的capacity也有两个维度. 其它部分没有太大改变.
    仅在内循环capacity时需要循环m n两个维度上的重量.
  Problem Desc:
    Type: 0/1 Knapsack 0/1背包问题二维版本
    Prob: max number of items 最值问题
  Template:
    DP[i][j]: the max number of items given capacity of i and j
    Transition: DP[i][j] = max(DP[i][j], DP[i-item[0]][j-item[1]]+1)
    Initial: DP=0
    Loop: 外层strs, 内层倒序capacity(嵌套两个维度)
  Complexity:
    Time: O(m*n*lenOfStrs)
    Space: O(m*n)
  '''
  def findMaxForm(self, strs, m, n):
    # define the target capacity
    capacity = [m, n]

    # initiate DP
    DP = [[0] * (n+1) for _ in range(m+1)]

    # loop to create DP
    for str in strs:
      n0 = str.count('0')
      n1 = str.count('1')
      for i in range(capacity[0], n0-1, -1):
        for j in range(capacity[1], n1-1, -1):
          # the boundary condition is included in loop conditions
          DP[i][j] = max(DP[i][j], DP[i-n0][j-n1]+1)
    
    # return DP[capacity] as problem required
    return DP[capacity[0]][capacity[1]]


## Run code after defining input and solver
input1 = ["10","0001","111001","1","0"]
input2 = 5
input3 = 3
solver = Solution().findMaxForm
print(solver(input1, input2, input3))