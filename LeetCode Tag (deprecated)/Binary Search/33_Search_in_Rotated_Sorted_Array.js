/**
 * You are given an integer array nums sorted in ascending order, and an integer target.
 * Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
 * If target is found in the array return its index, otherwise, return -1.
 * 
 * Example 1:
 * 
 * Input: nums = [4,5,6,7,0,1,2], target = 0
 * Output: 4
 */

var search = function(nums, target) {
    let left = 0;
    let right = nums.length-1;
    
    /*// This is a conventional binary search in a sorted array
      // We will update the algorithm based on this form 
    while (left <= right) {
        let mid = Math.floor((left+right)/2);
        if (target === nums[mid])
            return mid;
            
        if (target < nums[mid]) {
            right = mid-1;
        } else {
            left = mid+1;
        }        
    }*/
    
    while (left <= right) {
        let mid = Math.floor((left+right)/2);
        if (target === nums[mid])
            return mid;
        
        // the left part is sorted
        if (nums[left] <= nums[mid]) {
            // check if in the sorted array or not
            if (target >= nums[left] && target < nums[mid] ) {
                right = mid - 1;
            // if not, them target is in the right array
            } else {
                left = mid + 1;
            }
        
        // the right part is sorted
        } else {
            // check if in the sorted array or not
            if (target <= nums[right] && target > nums[mid]) {
                left = mid + 1;
            // if not, them target is in the left array
            } else {
                right = mid - 1;
            }
        }
    }
    
    return -1;
};

const result = search([3,1], 1);
console.log(result);