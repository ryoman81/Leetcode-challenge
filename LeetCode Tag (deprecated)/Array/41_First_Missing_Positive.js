/**
 * Given an unsorted integer array, find the smallest missing positive integer.
 * 
 * Example 1:
 * Input: [1,2,0]
 * Output: 3
 * 
 * Example 2:
 * Input: [3,4,-1,1]
 * Output: 2
 * 
 * Example 3:
 * Input: [7,8,9,11,12]
 * Output: 1
 */

 /*
// O(nlogn)
var firstMissingPositive = function(nums) {
    // sort the current array O(nlogn)
    nums.sort((a,b) => a-b);
    
    // loop over and find the smallest missing part O(n)
    let smallest = 1;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] <= 0) continue;
        if (nums[i] > smallest) {
            return smallest;
        } else if (nums[i] === smallest) {
            smallest++;
        }
    }
    return smallest;
};
*/

// improvement of above solution should deal with sorting behavior O(n)
var firstMissingPositive = function(nums) {
    // doing a swap and let i to stay at the nums[i-1]
    let i = 0;
    while (i < nums.length) {
        // it requires three conditions when we put i in nums[i-1]
        // 1. i exists in nums and is a positive integer
        // 2. i should less than array size (otherwise we have no place to put it in)
        // 3. if i is not at the location nums[i-1]
        const crrVal = nums[i];
        if (crrVal > 0 && crrVal <= nums.length && crrVal !== nums[crrVal-1]) {
            nums[i] = nums[crrVal - 1];
            nums[crrVal - 1] = crrVal;
        } else {
            i++;
        }
    }

    // Now we can loop over the nearly sorted array to find the smallest missing integer
    for (let j = 0; j < nums.length; j++) {
        if (nums[j] !== j+1) return j+1;
    }

    return nums.length + 1;
};

const result = firstMissingPositive([3,2,7,5,11,34,58]);
console.log(result);
