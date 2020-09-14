/**
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
 */

var reverse = function(x) {
    const str = x.toString();
    let str_rvs = "";
    let result;
    if (str[0] === "-") {
        str_rvs = "-";
        for (let i = str.length-1; i >= 1; i--) {
            str_rvs += str[i];
        }
        result = Number(str_rvs);
    } else {
        for (let i = str.length-1; i >= 0; i--) {
            str_rvs += str[i];
        }
        result = Number(str_rvs);
    }
    
    let bigN = Math.pow(2, 31);
    if (result < -bigN || result > bigN-1) {
        result = 0;
    }
    
    return result;
};

const result = reverse(1534236469);
console.log(result);