/**
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
*/

// hashtable solution time O(n), space O(n)
const singleNumber = function(nums) {
    // create a hash table
    const hashTable = {};
    for (let i = 0; i < nums.length; i++) {
        if (!hashTable[nums[i]]) {
            hashTable[nums[i]] = [i];
        } else {
            hashTable[nums[i]].push(i);
        }
    }
    for (let key of Object.keys(hashTable)) {
        if (hashTable[key].length === 1) {
            return key;
        }
    }
};

console.log(singleNumber([1,1,2,2,3,3,4,4,5,6,6]));