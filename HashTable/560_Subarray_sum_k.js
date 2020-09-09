/**
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Input:nums = [1,1,1], k = 2
Output: 2
*/

// O(n^2)
const subarraySum = function(nums, k) {
    let count = 0;
    for (let i = 0; i < nums.length; i++) {
        let sum = 0;
        for (let j = i; j < nums.length; j++) {
            sum += nums[j];
            if (sum === k)
                count++;
        }
    }
    return count;
};

console.log(subarraySum([1,2,3],3))