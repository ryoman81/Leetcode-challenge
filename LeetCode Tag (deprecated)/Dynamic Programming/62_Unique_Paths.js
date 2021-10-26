/**
 * A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
 * The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
 * 
 * Example 1:
 * 
 * Input: m = 3, n = 7
 * Output: 28
 */


/*
// recursion time over limit
var uniquePaths = function(m, n) {
    const total = moveTo(m, n);
    return total;

    function moveTo (i, j) {
        if (i === 1 || j === 1) 
            return 1;

        return moveTo(i-1, j) + moveTo(i, j-1);
    }
};
*/

/*
// Recursion with DP: we must use cache to avoid recalculation
var uniquePaths = function(m, n) {
    const cache = {};
    const total = moveTo(m, n);
    return total;
    
    function moveTo (i, j) {
        if (i === 1 || j === 1) {
            return 1;
        } 
        
        // check if stored in cache
        const key = JSON.stringify([i,j]);
        if (key in cache) {
            return cache[key];
        }
        
        // if no cache then calculate it
        cache[key] = moveTo(i-1, j) + moveTo(i, j-1);
        return cache[key];
    }
};
*/


// Use DP without recursion (bottom-up)
var uniquePaths = function(m, n) {
    const dp = new Array(m).fill(1);
    for (let i in dp)
        dp[i] = new Array(n).fill(1);

    for (let i = 1; i < m; i++) {
        for (let j = 1; j < n; j++) {
            dp[i][j] = dp[i-1][j] + dp[i][j-1];
        }
    }
    
    return dp[m-1][n-1];
};

console.log(uniquePaths(8,4));