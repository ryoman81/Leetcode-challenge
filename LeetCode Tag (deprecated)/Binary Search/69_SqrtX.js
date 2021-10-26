/**
 * Implement int sqrt(int x).
 * Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
 * Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
 * 
 * Example 1:
 * 
 * Input: 4
 * Output: 2
 */

/*
// Brute force to search in all integers
var mySqrt = function(x) {
    let result = 1;
    while (true) {
        const val = result * result;
        if (val > x) return result - 1;
        result++;
    }
};
*/

// Binary Search, because the integers are sorted
var mySqrt = function(x) {
    if (x === 0) return 0;
    let left = 1;
    let right = x;

    while (left <= right) {
        const mid = (left+right)/2 | 0;
        const val1 = mid * mid;
        const val2 = (mid+1) * (mid+1);
        if (val1 < x && val2 > x || val1 === x) {
            return mid;
        }
        if (val1 < x) {
            left = mid + 1;
        } else {
            right = mid -1;
        }
    }
};