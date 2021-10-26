/**
 * Given a collection of intervals, merge all overlapping intervals.
 * 
 * Example 1:
 * 
 * Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
 * Output: [[1,6],[8,10],[15,18]]
 * Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
 */

var merge = function(intervals) {
    if (intervals.length < 2) return intervals;
    
    intervals.sort((a, b) => a[0]-b[0]);        // O(nlogn)
    
    const result = [intervals[0]];              // sp: O(n)
    let p_org = 1;
    let p_result = 0;
    while (p_org < intervals.length) {          // O(n)
        // if need to merge
        if (intervals[p_org][0] <= result[p_result][1]) {
            result[p_result][1] = Math.max(intervals[p_org][1], result[p_result][1]);
        } else {
            result.push(intervals[p_org]);
            p_result++;
        }
        p_org++;
    }
    
    return result;
};