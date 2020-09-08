/**
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
*/

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

const maxSubArray = function(nums) {
    if (nums.length === 0) return false;
    

    return maxSum;
};

const maxValue = maxSubArray([-2,1]);
console.log(maxValue);