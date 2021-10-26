/**
 * The count-and-say sequence is the sequence of integers with the first five terms as following:
 * 
 * 1.     1
 * 2.     11
 * 3.     21
 * 4.     1211
 * 5.     111221
 * 1 is read off as "one 1" or 11.
 * 11 is read off as "two 1s" or 21.
 * 21 is read off as "one 2, then one 1" or 1211
 */

/*
// iterative approve
var countAndSay = function(n) {
    if (n === 1) return "1";
    
    let crrSay = "1";
    for (let i = 2; i <= n; i++) {
        let newSay = "";
        let j = 0;
        while(crrSay[j] !== undefined) {    
            if (crrSay[j] !== crrSay[j+1]){
                newSay += ("1" + crrSay[j]);
                j++;
            } else {
                let k = 1;
                while(crrSay[j] === crrSay[j+1+k]) {
                    k++;
                }
                newSay += ((k+1) + crrSay[j]);
                j += (k+1);    
            }
        }
        crrSay = newSay;
    }
    return crrSay;
};
*/

// recursive approve
var countAndSay = function(n) {
    if (n === 1) return "1";
    
    let cnt = n;
    
    const findSay = (crrSay) => {
        if (cnt === 1) {
            return crrSay;
        }
        
        let newSay = "";
        let j = 0;
        while(crrSay[j] !== undefined) {    
            if (crrSay[j] !== crrSay[j+1]){
                newSay += ("1" + crrSay[j]);
                j++;
            } else {
                let k = 1;
                while(crrSay[j] === crrSay[j+1+k]) {
                    k++;
                }
                newSay += ((k+1) + crrSay[j]);
                j += (k+1);    
            }
        }
        
        cnt--;
        return findSay(newSay);
    }
    
    return findSay("1");
};


const result = countAndSay(5);
console.log(result);