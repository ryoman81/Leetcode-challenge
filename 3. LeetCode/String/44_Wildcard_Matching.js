/**
 * Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.
 * '?' Matches any single character.
 * '*' Matches any sequence of characters (including the empty sequence).
 * The matching should cover the entire input string (not partial).
 * Note:
 * s could be empty and contains only lowercase letters a-z.
 * p could be empty and contains only lowercase letters a-z, and characters like ? or *.
 * 
 * Example:
 * 
 * Input:
 * s = "adceb"
 * p = "*a*b"
 * Output: true
 * Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
 */

/* 
    My note: the key of this algorithm is by using pointers, 

*/


var isMatch = function(s, p) {
    let pp = 0;         // pattern pointer
    let sp = 0;         // string pointer
    let ss = sp;        // substring pointer
    let star = null;    // star pointer

    // loop over the string (my previous trial was to loop over the pattern)
    while (sp < s.length) {
        // if current pattern matches string
        if (p[pp] === s[sp] || p[pp] === "?") {
            // advance both pattern and string pointer and continue
            pp++; sp++; continue;
        }

        // if current pattern is star
        if (p[pp] === "*") {
            // record the new star location and advance pattern pointer
            star = pp; pp++;
            // record update the substring pointer to the current location
            ss = sp; 
            continue;
        }

        // if star exist
        if (star !== null) {
            // hold the pattern pointer to the next of the star
            pp = star + 1;
            // advance substring pointer and update string pointer
            ss++; sp = ss;
            continue;
        }

        // if none star exist and no match success
        return false;
    }

    // if use up string pointer then check if any remaining star
    while (p[pp] === "*") pp++;
    // check if now pp is undefined
    return !p[pp] ? true : false;
};

console.log(isMatch("aaaa", "***a"));