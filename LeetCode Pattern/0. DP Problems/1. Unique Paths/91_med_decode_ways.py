'''
A message containing letters from A-Z can be encoded into numbers using the following mapping:
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters 
using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:
"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".
Given a string s containing only digits, return the number of ways to decode it.
The answer is guaranteed to fit in a 32-bit integer.

Example 1:

Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:
Input: s = "0"
Output: 0
Explanation: There is no character that is mapped to a number starting with 0.
The only valid mappings with 0 are 'J' -> "10" and 'T' -> "20", neither of which start with 0.
Hence, there are no valid ways to decode this since all digits need to be mapped.

Example 4:
Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
 
Constraints:
1 <= s.length <= 100
s contains only digits and may contain leading zero(s).
'''


class Solution:
  '''
  MY CODE VERSION
  Thought:
    Dynamic Programming template:
      State: DP[i] - number of ways to interpret a string at s[i]
      Transition:
        - DP[i] = DP[i-1] ----> s[i] 可以被翻译, s[i-1]+s[i] 不可以被翻译
        - DP[i] = DP[i-2] ----> s[i] = 0, 但 s[i-1]+s[i] 在一起可以被翻译
        - DP[i] = DP[i-1] + DP[i-2] ----> s[i] 可以被翻译, s[i-1]+s[i] 也可以被翻译
        - DP[i] = 0 ----> s[i] = 0, 并且 s[i-1]+s[i] 在一起不能被翻译
      Initial states: DP[0] = 1
  Complexity:
    Time: O(n)
    Space: O(n) - space optimization available
  '''
  def numDecodings(self, s):
    # because leading by '0' is always invalid
    if s[0] == '0':
      return 0

    # initialize DP with DP[0] = 1 (第一位若不是'0'则只能翻译出一种可能)
    n = len(s)
    DP = [0] * n
    DP[0] = 1

    for i in range(1, n):
      # s[i] itself can be decoded
      if s[i] != '0':
        DP[i] = DP[i-1]
      
      # s[i-1:i+1] may also be decoded
      if i<n and 10<=int(s[i-1:i+1])<=26:
        if i == 1:
          DP[i] += 1
        else:
          DP[i] += DP[i-2]  

    return DP[n-1]


## Run code after defining input and solver
input1 =  "0"
solver = Solution().numDecodings
print(solver(input1))