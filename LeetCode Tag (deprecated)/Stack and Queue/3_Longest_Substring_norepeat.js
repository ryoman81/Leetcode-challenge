/**
Given a string s, find the length of the longest substring without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
*/

var lengthOfLongestSubstring = function(s) {
    
    const queue = [];
    let longest = 0;
    
    for (let i = 0; i < s.length; i++) {        // O(n)
        let index = queue.indexOf(s[i]);
        if (index === -1) {
            queue.push(s[i]);
            if (queue.length > longest){
                longest = queue.length;
            }
        } else {
            queue.splice(0, index+1);
            queue.push(s[i]);
        }
    }
    
    return longest;
};

const result = lengthOfLongestSubstring("pwwkew");
console.log(result);