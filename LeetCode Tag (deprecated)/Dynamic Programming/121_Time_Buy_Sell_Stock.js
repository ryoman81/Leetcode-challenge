/**
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction, design an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
 */

const maxProfit = function(prices) {
    let minPrice = prices[0];     // in DP, this is a memorization to be cached
    
    let maxDiff = 0;
    for (let i = 0; i < prices.length; i++) {
        // this is the soul in DP to update memorized information dynamically
        if (prices[i] < minPrice)
            minPrice = prices[i];

        if (prices[i] - minPrice > maxDiff) {
            maxDiff = prices[i] - minPrice;
        }
    }

    return maxDiff;
};

console.log(maxProfit([-2,-3]));