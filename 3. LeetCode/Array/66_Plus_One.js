/**
 * Given a non-empty array of digits representing a non-negative integer, increment one to the integer.
 * The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
 * You may assume the integer does not contain any leading zero, except the number 0 itself.
 * 
 * Example 1:
 * 
 * Input: digits = [1,2,3]
 * Output: [1,2,4]
 */

var plusOne = function(digits) {
    const len = digits.length;
    for (let i = len-1; i >= 0; i--) {
        const num = digits[i] + 1;
        if (num < 10) {
            digits[i] = num;
            return digits;
        } else {
            digits[i] = 0;
        }
    }
    
    return [1, ...digits];
};