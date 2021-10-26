/**
 * Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
 * 
 * Example 1:
 * 
 * Input: s = "()[]{}"
 * Output: true
 */

var isValid = function(s) {
    if (s.length <= 1){
        return false;
    }
    const stack = [s[0]];
    
    for (let i = 1; i < s.length; i++) {
        stack.push(s[i]);
        const right = stack[stack.length-1];
        const left = stack[stack.length-2];

        if (left === "(" && right === ")"){
            stack.pop();
            stack.pop();
        }
        if (left === "[" && right === "]"){
            stack.pop();
            stack.pop();
        }
        if (left === "{" && right === "}"){
            stack.pop();
            stack.pop();
        }
    }
    return stack.length === 0? true: false;
};

console.log(isValid("[()]{}"));