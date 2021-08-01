'''
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Example 3:
Input: s = "a"
Output: "a"

Example 4:
Input: s = "ac"
Output: "a"
 
Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),
'''


class Solution:
  '''
  MY CODE VERSION
  DP solution template:
    DP[i][j]:   if str[i:j+1] is palindrome
    Transition: DP[i][j] = DP[i+1][j-1] && (str[i]==str[j])
    Init:       DP=False, DP[i][i] = True
    Condition:  这是本题当中非常tricky的点, 循环的顺序, i和j大小条件都影响
  Complexity:
    Time: O()
    Space: O()
  '''
  def longestPalindrome(self, s):
    n = len(s)

    # Initialize DP
    DP = [[False] * n for _ in range(n)]
    for i in range(n):
      DP[i][i] = True

    # a record for the maximum length result
    result = ""

    # loop to create DP
    for i in range(n-1, 0, -1):
      for j in range(0, n-1):
        # 对于子字串长度大于等于1时, 可直接应用状态转移方程
        if i+1 <= j-1:
          DP[i][j] = DP[i+1][j-1] and s[i]==s[j]
        # 对于子字符串长度等于1时, 则 i->j 一定为一个回文
        elif j-i == 1:
          DP[i][j] = s[i]==s[j]
        else:
          continue

        if j - i >= len(result):
          result = s[i:j+1]
    return result


## Run code after defining input and solver
input = "aaabcbaba"
solver = Solution().longestPalindrome
print(solver(input))