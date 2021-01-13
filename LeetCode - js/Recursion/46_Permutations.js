/**
 * Given a collection of distinct integers, return all possible permutations.
 * 
 * Example:
 * 
 * Input: [1,2,3]
 * Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 */

var permute = function(nums) {
    const result = [];
    search([], nums);
    return result;

    function search (crr, rest) {
        if (!rest.length) {
            result.push(crr);
            return;
        }
        
        for (let i = 0; i < rest.length; i++) {
            const newCrr = [...crr, rest[i]];
            const newRest = [...rest.slice(0, i), ...rest.slice(i+1)];
            search(newCrr, newRest);
        }
    }
};

console.log(permute([3,5,8]));