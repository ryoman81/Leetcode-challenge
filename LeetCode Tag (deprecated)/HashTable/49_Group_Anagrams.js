/**
 * Given an array of strings strs, group the anagrams together. You can return the answer in any order.
 * An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
 * 
 * Example 1:
 * 
 * Input: strs = ["eat","tea","tan","ate","nat","bat"]
 * Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
 */

var groupAnagrams = function(strs) {
    const table = {};
    const result = [];
    
    for (let i = 0; i < strs.length; i++) {
        // "tea" -> ['a', 'e', 't'] -> "aet"
        const str = [...strs[i]].sort().join("");
        // if table contain this typing string or not
        if (table[str]) {
            table[str].push(strs[i]);
        } else {
            table[str] = [strs[i]];
        }
    }
    
    for (let key of Object.keys(table))
        result.push(table[key]);
    
    return result;
};