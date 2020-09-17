/**
 * Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
 * 
 * Example 1:
 * 
 * Input: "III"
 * Output: 3
 */

var romanToInt = function(s) {
    const table = {
        I: 1,
        V: 5,
        X: 10,
        L: 50,
        C: 100,
        D: 500,
        M: 1000
    }
    let roman = 0;
    for (let i = 0; i < s.length; i++) {
        if (table[s[i+1]] > table[s[i]]) {
            roman += table[s[i+1]] - table[s[i]];
            i++;
        } else {
            roman += table[s[i]];
        }
    }
    return roman;
};

const result = romanToInt("MCMXCIV");
console.log(result);