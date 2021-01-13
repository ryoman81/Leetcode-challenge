// 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 ...

// memorization cache
const cache = {};

function fibonacci (n) {
    // load the cache if fib(n) has been calculated before
    if (n in cache) {
        return cache[n];
    }
    // base case that stops recursion
    if (n < 2) {
        return n;
    }
    // otherwise store the result in a cache
    cache[n] = fibonacci(n-1) + fibonacci(n-2);
    // then return the recursion case
    return cache[n];
}

const result = fibonacci(6);
console.log(result);