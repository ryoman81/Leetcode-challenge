/**
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
 */

 /*
// Brute Force: very slow and O(n^3)
var longestPalindrome = function(s) {
    if(s.length === 0)
        return "";
    let result = s[0];
    for (let i = 0; i < s.length; i++) {
        for (let j = i+1; j < s.length; j++) {
            const substring = s.substring(i, j+1);
            if (checkIfPalindromic(substring)) { 
                if (substring.length > result.length) {
                    result = substring;
                }
            }
        }
    }
    return result; 
    
    function checkIfPalindromic (substring) {
        let i = 0;
        let j = substring.length - 1;
        while (i < j) {
            if (substring[i] !== substring[j])
                return false;
            i++; j--;
        }
        return true;
    }
};
*/

var longestPalindrome = function(s) {
    let palindrome = "";
    
    for (let i = 0; i < s.length; i++) {
        // check current i around
        let currStr1 = s[i];
        let currStr2 = s[i];
        let j;
        // scenario 1: s[i] as centrual search around
        j = 1;
        while (true) {
            if (i-j < 0) break;
            if (s[i-j] === s[i+j]) {
                currStr1 = s.substring(i-j, i+j+1);
                j++;
            } else {
                break;
            }
        }
        // scenario 2: middle of s[i] and s[i+1] as centrual
        j = 1;
        if (s[i] === s[i+1]) {
            currStr2 = s.substring(i, i+2);
            while (true) {
                if (i-j < 0) break;
                if (s[i-j] === s[i+1+j]) {
                    currStr2 = s.substring(i-j, i+j+2);
                    j++;
                } else {
                    break;
                }
            }
        }

        const longerStr = (currStr1.length>currStr2.length)? currStr1: currStr2;
        
        if (longerStr.length > palindrome.length)
            palindrome = longerStr;
    }
    
    return palindrome;
}

const result = longestPalindrome("abba");
console.log(result);