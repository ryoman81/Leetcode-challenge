/**
 * Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
 * Your algorithm's runtime complexity must be in the order of O(log n).
 * If the target is not found in the array, return [-1, -1].
 * 
 * Example 1:
 * 
 * Input: nums = [5,7,7,8,8,10], target = 8
 * Output: [3,4]
 */


var searchRange = function(nums, target) {
    let start_left = 0;
    let start_right = nums.length - 1;
    
    let end_left = 0;
    let end_right = nums.length - 1;
    
    let find_start = 0;
    let find_end = 0;
    
    const result = [-1, -1];
    
    while (start_left <= end_right) {
        if (find_start && find_end) break;

        let start_mid = Math.floor((start_left+start_right)/2);
        let end_mid = Math.floor((end_left+end_right)/2);
        
        if (nums[start_mid] === target && nums[start_mid-1] !== target) {
            result[0] = start_mid;
            find_start = 1;
        } else if (nums[start_mid] < target) {
            start_left = start_mid + 1;
        } else {
            start_right = start_mid - 1;
        }

        if (nums[end_mid] === target && nums[end_mid+1] !== target) {
            result[1] = end_mid;
            find_end = 1;
        } else if (nums[end_mid] > target) {
            end_right = end_mid - 1;
        } else {
            end_left = end_mid + 1;
        }
    }

    return result;
};

const result = searchRange([], 6);
console.log(result);