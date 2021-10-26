/**
Write a function that reverses a string. The input string is given as an array of characters char[].
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
You may assume all the characters consist of printable ascii characters.

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

*/

const reverseString = function(s) {
    if (s.length < 1) {
        return s;
    }

    return [s.pop(), ...reverseString(s)];
};
console.log(reverseString(['h','e','l','l','o']));

const reverseString2 = function (s) {
    let pointer_left = 0;
    let pointer_right = s.length-1;
    
    while (pointer_left <= pointer_right) {
        let temp = s[pointer_left];
        s[pointer_left] = s[pointer_right];
        s[pointer_right] = temp;
        pointer_left++;
        pointer_right--;
    }
};

s = ['h','e','l','l','o'];
reverseString2(s);
console.log(s)