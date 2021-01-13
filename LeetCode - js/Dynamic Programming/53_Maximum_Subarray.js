/**
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
*/

// a better solution O(n)
const maxSubArray = function(nums) {
    let prev = 0;
    let max = -Infinity;

    for (let i = 0; i < nums.length; i++) {
        // if previous sum is less than the current number 
        // then start new for the current number
        // This is DP that dynamically update prev which is a memorization
        if (prev + nums[i] < nums[i]) {
            prev = nums[i];
        } else {
            prev = prev + nums[i];
        }
        // update max number
        max = (max > prev)? max: prev;
    }
    return max;
}

/*
// very slow n + (n-1) + (n-2) + ... + 1 = O(n^2)
const maxSubArray = function(nums) {
    if (nums.length === 0) return false;
    let maxSum = nums[0];
    for (let i = 0; i < nums.length; i++) {
        let sum = nums[i];
    
        for (let j = i; j < nums.length; j++) {
            if (j !== i) {
                sum += nums[j];
            }
            if (sum > maxSum) {
                maxSum = sum;
            }
        }
    }
    return maxSum;
};
*/

/*const maxSubArray = function(nums) {
    if (nums.length === 0) return false;
    if (nums.length === 1) return nums[0];
    // create an array to record accumulated sum
    const accSum = [nums[0]];
    for (let i = 1; i < nums.length; i++) {
        accSum.push(accSum[i-1] + nums[i]);
    }
    // find the max diff
    let maxDiff = Math.max(...accSum);
    let minSum = accSum[0];
    for (let i = 1; i < accSum.length; i++) {
        
        if (accSum[i] - minSum > maxDiff)
            maxDiff = accSum[i] - minSum;

        if (accSum[i] < minSum)
            minSum = accSum[i];
    }
    return maxDiff;
};
*/

const maxValue = maxSubArray([1,2]);
console.log(maxValue);