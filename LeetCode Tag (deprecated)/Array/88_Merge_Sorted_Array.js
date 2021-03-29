/**
 * Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
 * The number of elements initialized in nums1 and nums2 are m and n respectively.
 * You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
 * 
 * Example:
 * 
 * Input:
 * nums1 = [1,2,3,0,0,0], m = 3
 * nums2 = [2,5,6],       n = 3
 * 
 * Output: [1,2,2,3,5,6]
 */

var merge = function(nums1, m, nums2, n) {
    let pointer1 = m-1;
    let pointer2 = n-1;
    let p = n+m-1;
    
    while (pointer2 >= 0) {
        if (nums2[pointer2] > nums1[pointer1] || pointer1 === -1) {
            nums1[p] = nums2[pointer2];
            pointer2--;
            p--;
        } else {
            nums1[p] = nums1[pointer1];
            pointer1--;
            p--;
        }
    }
    return nums1;
};

console.log(merge([0], 0, [1], 1));