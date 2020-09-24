/**
 * Given n non-negative integers representing an elevation map where the width of each bar is 1, 
 * compute how much water it is able to trap after raining.
 * 
 * Example:
 * 
 * Input: [0,1,0,2,1,0,1,3,2,1,2,1]
 * Output: 6
 */


// two pointers: O(n)
// start from two ends, and find lowland in each part
var trap = function(height) {
    let left = 0;
    let right = height.length-1;
    let sum = 0;
    // before two pointers meet
    while (left < right) {
        // for the left part
        if (height[left+1] >= height[left]) {
            left++;
        } else { // if right side lower than the left
            let cnt = 1;
            let localSum = 0;
            while (left+cnt <= right) {
                if (height[left+cnt] >= height[left]) break;
                localSum += height[left] - height[left+cnt];
                cnt++;
            }
            // if left pointer is still less than right or equal then update
            if (left + cnt <= right) {
                sum += localSum;
                left += cnt;
            }
        }
        // for the right part do the same things
        if (height[right-1] >= height[right]) {
            right--;
        } else {
            let cnt = 1;
            let localSum = 0;
            while (right - cnt >= left) {
                if (height[right-cnt] >= height[right]) break;
                localSum += height[right] - height[right-cnt];
                cnt++;
            }
            if (right - cnt >= left) {
                sum += localSum;
                right -= cnt;
            }
        }
    }
   return sum;
};

const result = trap([3,6,3,4]);
console.log(result);