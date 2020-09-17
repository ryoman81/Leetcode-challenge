/**
 * Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
 * n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
 * Find two lines, which together with x-axis forms a container, such that the container contains the most water.
 * 
 * Example:
 * 
 * Input: [1,8,6,2,5,4,8,3,7]
 * Output: 49
 */

// O(n^2) brute force
/*var maxArea = function(height) {
    let maxWater = 0;
    
    for (let i = 0; i < height.length; i++) {
        for (let j = i+1; j < height.length; j++) {
            const w = j - i;
            const h = (height[i] > height[j])? height[j]: height[i];
            
            if (w*h > maxWater)
                maxWater = w*h;
        }
    }
    return maxWater;
};*/

// two pointers O(n)
var maxArea = function(height) {
    let maxWater = 0;
    let left = 0;
    let right = height.length-1;
    
    while (left < right) {
        const w = right - left;
        const h = (height[left] > height[right])? height[right]: height[left];
        const v = w * h;
        
        if (v > maxWater)
            maxWater = v;
        
        if (height[left] > height[right]) {
            right--;
        } else {
            left++;
        }
    }
    
    return maxWater;
};