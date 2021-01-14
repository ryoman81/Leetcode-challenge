'''
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''

#### Define the answer code class named Solution
class Solution:
    '''
    MY CODE VERSION
    Thought:
      1. Using a list as sliding window
      2. Right move the right-side to meet incoming char
      3. Check if the incoming char exists in the window
      4. If exists then move left-side to this new location
    Complexity:
      Time: O(n)
      Space: O(n)
    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        window = []     # O(n)
        # loop over string
        for i in range(len(s)):     # O(n)
            # check if upcoming char is within window
            # have to use try-except since index() will return ValueError
            try:
                index = window.index(s[i])
            except ValueError:
                index = -1
            # push new char to window queue
            window.append(s[i])
            # if not append char to the window
            if index == -1:
                # update longest if substr is longer
                if len(window) > longest:
                    longest = len(window)
            # if exist then cut the front half till index
            else:
                window = window[index+1:]
        return longest

    '''
    THE OPTIMAL CODE VERSION
    Improvement:
      1.
    Thought:
      1. Using a list as sliding window
      2. Right move the right-side to meet incoming char
      3. Check if the incoming char exists in the window
      4. If exists then move left-side to this new location
    Complexity:
      Time: 
      Space:
    '''
    def lengthOfLongestSubstringOpt(self, s: str) -> int:
        return 0


#### Run code after defining input and solver
input = 'fdgdsgsdfg'
solver = Solution().lengthOfLongestSubstring
print(solver(input))