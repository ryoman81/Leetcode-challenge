// Write two functions that finds the factorial of any number. One should use recursive, the other should just use a for loop
// Input 5
// Output 5!

function findFactorialRecursive(number) {
    if (number < 2) {
        return number;
    }
    return number * findFactorialRecursive(number-1);
}
  
function findFactorialIterative(number) {
    let answer = number;
    for (let i = number-1; i > 0; i--) {
        answer *= i;
    }
    return answer;
}
  
console.log(findFactorialIterative(4));     // Time O(n)
console.log(findFactorialRecursive(4));     // Time O(n)
