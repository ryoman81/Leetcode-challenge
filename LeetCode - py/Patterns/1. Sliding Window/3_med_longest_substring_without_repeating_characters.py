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
    def lengthOfLongestSubstring(self, s: str):
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
      - Since a window array may take more space, using HashTable can benefit
      - HashTable also resolved index() problem in Python (no need to use try-except-catch)
      - Here use left and right pointers
    Thought:
      1. Loop over to move right pointer till end
      2. Check if the incoming char is in hashtable
      3. If exist, move left pointer rightwards and remove other record until meet right
    Complexity:
      Time: O(n)
      Space: O(1)
    '''
    def lengthOfLongestSubstringOpt(self, s: str):
        hashTable = {}
        left = 0
        result = 0
        # right pointer loops over string
        for right in range(len(s)):
            # check if right pointer in table
            if s[right] in hashTable:
                # if in table then move left pointer to there
                # at the same time remove all records between left and right
                index = hashTable[s[right]]
                while left <= index:
                    del hashTable[s[left]]
                    left += 1
            # record the current right pointer
            hashTable[s[right]] = right
            # update longest if have
            if (right-left+1) > result:
                result = right-left+1
        return result


## Run code after defining input and solver
input = ''
solver = Solution().lengthOfLongestSubstringOpt
print(solver(input))