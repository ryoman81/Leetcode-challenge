/**
 * Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
 * Find all unique triplets in the array which gives the sum of zero.
 * Notice that the solution set must not contain duplicate triplets.
 * 
 * Example 1:
 * 
 * Input: nums = [-1,0,1,2,-1,-4]
 * Output: [[-1,-1,2],[-1,0,1]]
 */

/*// O(n^2) exeeded time limit may be due to JSON operation
var threeSum = function(nums) {
    if (nums.length < 3) return [];
    const result = [];
    const result_string = {};
    
    // create a hash table
    // here for the two sum problem, we can either use hashtable or two pointers
    const table = {};
    for (let i = 0; i < nums.length; i++) {
        if (table[nums[i]]) {
            table[nums[i]].push(i);
        } else {
            table[nums[i]] = [i];
        }
    }
    
    let a, b, c;
    for (let i = 0; i < nums.length; i++) {
        a = nums[i];
        // searching two sum problem
        for (let j = i+1; j < nums.length; j++) {
            b = nums[j];
            // find c where index > j that match
            c = -a-b;
            if (table[c] && Math.max(...table[c]) > j) {
                const cand = [a, b, c].sort((a,b) => a-b);
                const cand_str = JSON.stringify(cand);
                // check if duplicated
                if (!result_string[cand_str]) {
                    result.push(cand);
                    result_string[cand_str] = j;
                }
            }
        }
    }
    
    return result;
};*/

// should do a tricky part to avoid dupl
const threeSum = function (nums) {
    if (nums.length < 3) return [];
    const result = [];

    // !! sorted input array
    // so the first part are all negative numbers
    // we only need to loop over these part until i becomes positive
    nums.sort((a,b) => a-b);

    let i = 0;
    while (nums[i] <= 0) {
        // another smart part
        // if the current number is equal to the last then we skip to avoid duplicate
        if (i > 0 && nums[i] === nums[i-1]) {
            i++;
            continue;
        }
        
        // this time we use two pointers method
        // remember two pointers is a good way to do with sorted array
        let left = i+1;
        let right = nums.length-1;
        while (left < right) {
            const sum = nums[i] + nums[left] + nums[right];
            if (sum === 0) {
                result.push([nums[i], nums[left], nums[right]]);
                left++;
                right--;
                // control dupl numbers
                while (nums[left] === nums[left-1])
                    left++;
                while (nums[right] === nums[right+1])
                    right--;
            } else if (sum < 0) {
                left++;
            } else {
                right--;
            }   
        }

        i++;
    }

    return result;
}

const result = threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]);
console.log(result);