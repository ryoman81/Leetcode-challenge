/**
 * Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
 * Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
 * 
 * Example 1:
 * 
 * Input: [1,1,2]
 * Output: [1,2]
 */

var removeDuplicates = function(nums) {
    if (nums.length < 2) {
        return nums.length;
    }
    let last = nums[0];
    let index = 1;
    while(nums[index] !== undefined) {
        if (nums[index] === last) {
            nums.splice(index,1);
        } else {
            last = nums[index];
            index++;
        }
    }
    
    return nums.length;
};