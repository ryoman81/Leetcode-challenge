/**
 * Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
 * 
 * Example:
 * 
 * Input: "23"
 * Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
 */

var letterCombinations = function(digits) {
    const table = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }
    
    const findCombination = (arr1, arr2) => {
        const array = [];
        if (arr1.length === 0) {
            return arr2;
        }
        for (let n1 of arr1) {
            for (let n2 of arr2)
                array.push(n1+n2);
        }
        return array;
    }
    
    let output = [];
    for (let i = 0; i < digits.length; i++) {
        output = findCombination (output, table[digits[i]]);
    }
    
    return output;
};

result = letterCombinations("234");