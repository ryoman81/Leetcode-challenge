/**
 * You are climbing a stair case. It takes n steps to reach to the top.
 * Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
 * 
 * Example 1:
 * 
 * Input: 2
 * Output: 2
 * Explanation: There are two ways to climb to the top.
 * 1. 1 step + 1 step
 * 2. 2 steps
 */

// !!!!!!!!!!!!!!!!
// This is just a Fabonacci problem

/*
// DP using Fibonacci approach O(n)
var climbStairs = function(n) {
    // dp[n] = dp[n-1] + d[n-2]
    if (n === 1) return 1;
    if (n === 2) return 2;
    
    const dp = [];
    dp.push(0);
    dp.push(1);
    dp.push(2);
    for (let i = 3; i <=n; i++) {
        dp[i] = dp[i-1] + dp[i-2];
    }
    
    return dp[n];
}
*/

// Combination solution (not listed in the solution)
var climbStairs = function(n) {
    const odd = n % 2;
    const numTwo = Math.ceil(n/2);
    
    let sum = 1;
    let head = odd? numTwo-1 : numTwo;
    let ass = numTwo;
    while (head >= 1) {
        sum += combination (head, ass);
        head--;
        ass++;
    }
    
    return sum;
    
    function combination (head, ass) {
        let base = ass;
        let top = head;
        let cnt = 1;
        for (let i = base-1, cnt = 1; i >= 1; i--, cnt++) {
            if (cnt === head) break;
            base *= i;
        }
        for (let i = top-1; i >= 1; i--)
            top *= i;
        return base/top;
    }
};

const result = climbStairs(6);
console.log(result);