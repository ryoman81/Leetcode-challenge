/**
 * Write a function to find the longest common prefix string amongst an array of strings.
 * If there is no common prefix, return an empty string "".
 * 
 * Example 1:
 * 
 * Input: ["flower","flow","flight"]
 * Output: "fl"
 */

 // Vertical search O(MN) M = length of first tring, N = number of strings
var longestCommonPrefix = function(strs) {
    if (strs.length === 0) return "";
    let prefix = "";

    for (let i = 0; i < strs[0].length; i++) {
        const letter = strs[0][i];
        let pass = true;
        for (let j = 1; j < strs.length; j++) {
            const str = strs[j];
            if (str[i] !== letter) {
                pass = false;
                break;
            }
        }  
        if (pass) {
            prefix += letter;
        } else {
            break;
        }
    }
    
    return prefix; 
};