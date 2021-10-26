/**
 * 
 * Implement pow(x, n), which calculates x raised to the power n (i.e. xn).
 * 
 * Example 1:
 * 
 * Input: x = 2.00000, n = 10
 * Output: 1024.00000
 */

var myPow = function(x, n) {
    let power, base;
    if (n === 0) {
        return 1;
    } else if (n < 0) {
        power = -n;
        base = 1/x;
    } else {
        power = n;
        base = x;
    }
    
    let result = findPow(power);

    function findPow(p) {
        if (p === 1) return base;

        if (p%2) {
            return findPow(p-1)*base;
        } else {
            return findPow(p/2)**2;
        }
    }
    return result;
};

console.log(myPow(3, 3));