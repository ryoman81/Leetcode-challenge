/**
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature.
If there is no future day for which this is possible, put 0 instead.
For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].
Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
*/

/*// O(n^2)
const dailyTemperatures = function(T) {
    const outval = [];
    
    for (let i = 0; i < T.length; i++) {
        let days = 0;
        
        for (let j = i+1; j < T.length; j++) {
            days++
            if (T[j] > T[i]) break;
            if (j === T.length-1) days = 0;
            
        }
        outval.push(days);
    }
    return outval;
};
*/

// O(n)
const dailyTemperatures = function(T) {
    
    const hashTable = {};
    for (let i = 0; i < T.length; i++) {
        if (!hashTable[T[i]]) {
            hashTable[T[i]] = [i];
        } else {
            hashTable[T[i]].push(i);
        }
    }
    const outval = [];
    for (let i = 0; i < T.length; i++) {
        
        const cand = [];
        for (let j = T[i]+1; j < 101; j++) {
            // if this temp exists in the table
            if (hashTable[j]) {
                const ind = hashTable[j];
                for (let k = 0; k<ind.length; k++) {
                    if (ind[k] > i) cand.push(ind[k]);
                }
            }
        }
        let days;
        if (cand.length === 0) {
            days = 0
        } else {
            days = Math.min(...cand) - i;
        }
        outval.push(days);
    }
    return outval;
};

console.log(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]));