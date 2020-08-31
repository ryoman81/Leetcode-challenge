/*
Leetcode 1: Two Sum

Given an array of integers nums and and integer target, return the indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
*/ 

const nums = [];
const target = 9;

// Brute force: loop over array O(n^2)
const twoSum1 = function(nums, target) {
    for (let i = 0; i < nums.length; i++) {
        for (let j = i+1; j < nums.length; j++) {
            if (nums[i] + nums[j] === target)
                return [i,j];
        }
    }
    // if no result
    return [false, false];
};

// Create Hash table first O(n)
const twoSum2 = function(nums, target) {
    // create a hash table to store the key-value in nums: spacing O(n)
    const hashTable = {};
    for (let i = 0; i < nums.length; i++) {
        hashTable[nums[i]] = i;
    }
    for (let i = 0; i < nums.length; i++) {
        const diff = target - nums[i];
        if (hashTable[diff] === undefined) continue;
        if (hashTable[diff] === i) continue;
        return [i, hashTable[diff]];
    }
    // if no result
    return [false, false];
};

const t0 = new Date().getTime();
const result = twoSum1 (nums, target);
const t1 = new Date().getTime();

console.log(result, t1-t0);