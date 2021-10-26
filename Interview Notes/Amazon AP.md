# Coding: Topic Pattern Summary

## Dynamic Programming
```
DP has a very strong pattern. The questions such as XX subarray, unique path, or many recursively solved problems can be resolved by iterative DP. 

1. Define the cache [DP]
   Usually DP memorize the state at ith iteration. 
   It can be the summation from 0 to i, or total possible solution at ith step.
2. Determine state transformation
   DP[i] can be found the relationship with pervious states such as
      DP[i] = DP[i-1] + DP[i-2], or 
      DP[i] = DP[i-1] + arr[i]
3. Construct an iterative approach (not recursive approach).
```
53. Maximum Subarray (*easy*)
> Use an accumulative sum array [DP] to memorize the sum along. Then, at each iteration, the maximum sum can only be with max(dp[i-1]+nums[i], nums[i])
152. Maximum Product Subarray (*med*)
> Interesting topic and similar to 53. But we need to maintain two DP arrays.
> - DP1[i] maintain the max positive mul result in [0,i]
> - DP2[i] maintain the min negative mul result in [0,i]
> at each iteration the final result can only be with max(DP1[i-1]*nums[i], DP2[i-1]*nums[i], nums[i])
70. Climbing Stairs (*easy*)
> Use a memory array [DP] to memorize the number of possible solution to the ith stair. Covert to a Fibonacci problem. dp[i] = dp[i-1]+dp[i-2]
62. Unique Paths (*med*)
> Similar to 70, use a matrix [DP] to store the number of possible steps to dp[i][j]. The result should be dp[m-1][n-1]
377. Combination Sum IV (*med*)
> Similar to climb stairs and path problem.
> - Use a DP to memorize the solution numbers dp[i].
> - Loop over numerically from 1 to target.
> - For each iteration, loop over the nums, and find the accumulative solutions,
> - where dp[i] += dp[i-a], a is from nums.
304. Range Sum Query 2D
> The requirement for this problem is to reuse the sumRegion for multiple times for an instance. Very easy to use 2D matrix [DP] to cache the sumation from (0,0) to (i,j).
139. Word Break (*med*)
> - DP[i] is built to memorize if s[0:i) is separable and can be matched to dictionary. Hence, We loop over i to construct DP
> - For each iteration, we will use another loop to check if substring in s[0,j) and and its remaining part [j, i-j) is in the dictionary or DP memorization.
5. Longest Palindromic Substring (*med*)
> Actually, search from center is more straightforward than DP for this question.

## DFS/BFS
```
DFS usually works with recursion. node.left in recursion will lead to the most left leaf.
A very brilliant explanation of DFS: https://www.youtube.com/watch?v=W9F8fDQj7Ok 
BFS usually works with iteration and Queue. Queue will record all nodes in current level.
```
112. Path Sum (*easy*)
```js
const hasPathSum = function(root, sum) {
    if (!root) 
        return false;
    if (!root.left && !root.right && root.val == sum )
        return true;
    return hasPathSum(root.left, sum - root.val) || 
           hasPathSum(root.right, sum - root.val);
};
```
107. Binary Tree Level Order Traversal II (*easy*)
```js
queue.push(root);
while (queue.length > 0) {
    const currLevel = [];
    for (let i = queue.length; i > 0; i--) {
        const crrNode = queue.shift();
        currLevel.push(crrNode.val);
        if (crrNode.left) queue.push(crrNode.left);
        if (crrNode.right) queue.push(crrNode.right);
    }
    result.push(currLevel);
}
```
297. Serialize and Deserialize Binary Tree
> 
286. Walls and Gates
>
490. The Maze
> 


## Sorting
```js
// The principle of understanding sorting and its implementation is to know the algorithm complexity.
// The optimal sorting algorithm is merge sort O(nlogn). 
// The sorted array or data structure brings benefit to many applications usually reduces searching and traversal to O(logn).
mergeSort(arr) {
    // base case if the subarray length 1
    if (arr.length === 1) {
        return arr;
    }
    // split array into right and left
    const half_length = Math.ceil(arr.length / 2);
    const left = arr.slice(0, half_length);
    const right = arr.slice(half_length);
    // resursion step
    return merge(this.mergeSort(left), this.mergeSort(right));
    // in a merge function, just iteratively merge two arrays
}
```
49. Group anagrams (*med*)
> Sort each strings and do comparison.
56. Merge intervals (*med*)
> Make the starting time ascending, and loop over the the time interval.
253. Meeting Rooms II (*med*)
> Key for this question is to sort start time, end time into two arrays. And loop over the start time. 
> - Use a pointer refer to the current end time.
> - Use a variable to track the max room
> - In the for-loop of start time, every time meet a new start, we open a room (room++)
> - Every time the start time is greater than the current end time, we close a room (room--; p++)
75. Sort Colors (*med*)
> - A simple two-pass algorithm using count. First loop over and find the number of each colors. The second loop update current array based on the count of 0,1,2.
> - For one-pass solution, use **two pointers**. Since we only have 0,1,2. Loop over array from head, if 0, put to start, if 2 put to end, if 1 move on.
148. Sort List (*med*)
> The key is to implement merge sort on linked list. In recursive version, merge sort take time O(nlogn) and space (recursion stack = tree depth) O(logn)
280. Wiggle Sort (*med*)
> - One-loop, iterate members and swap based on the odd-even condition.
> - general solution, sort array O(nlogn), then swap each odd and even indexes from i=2

## Sliding window
```js
//In sliding window problem, we may best use a data structure (usually a queue) to maintain the content within the window. It depends on different problems, which requires different properties of window structure. The general queue one has a template as
const queue = arr.slice(0, k);
for (let i = k; i < arr.length; i++) {
    queue.push(arr[i]);     // push from right side
    queue.shift();          // pop from left side
}
```
3. Longest Substring Without Repeating Characters (*med*)
> use two indexes i = j initially. Advance j until duplicated term exist. Then advance i to the index of duplicate term.
239. Sliding Window Maximum (*hard*)
> For these three questions, the brute force solution is straightforward. just use a sliding window and internal functions to calculate the max, mean and median.
> - The key for 239 is to use a **decreasing monotonic queue** to maintain the window array.
> - Firstly, decreasing queue can maintain the max value in front of other elements.
> - Secondly, we can use shift to pop out max value when window slided. 
> - For this question, we can also use a **heap** structure.
480. Sliding Window Median (*hard*)
> Similar to the last one, we need to maintain a data structure of sliding window. The structure should be sorted initially. Each time moving the window, we insert the new value to the postion in a sorted structure. Here binary search is in use.
643. Maximum Average Subarray I (*easy*)
> Very easy pattern. Summarized in the mother scope.


## Binary Search
```js
//In topic scale, binary search usually reduces O(n) to O(logn). It is usually combined with two pointers or recursion solutions.

while (left <= right) {
    let mid = Math.floor((left+right)/2);
    if (target === nums[mid])
        return mid;
    if (target < nums[mid]) {
        right = mid-1;
    } else {
        left = mid+1;
    }        
}
```
33. Search in rotated sorted array (*med*)
> Little change in conventional BS template. Consider that one side is sorted then the pivot is on the other side.
74. Search a 2D Matrix (*med*)
> Linear search will check row index and col index to find the range that target within. Binary search O(logm+logn) only replace the range search by BF.
240. Search a 2D Matrix II (*med*)
> different from the last one, this question does not guarantee the beginning of next row is greater than the end of previous row. But it has a condition that each column is accending. The best practice is linear search and update row and col pointer down and right.
4. Median of Two Sorted Arrays (*hard*)
> Hard point is to achive O(log(m+n)). Otherwise O(m+n) can be easily achieved via combining two arrays and find the median. The mathematic for binary search version is too complicated.

## Linked List
```js
//The key for linked list is the pointers. In the most languages, pointers are only the references of current node (same to the tree and graph). No matter reverse, traversal, lookup or update, actions are conducted on the references. 

node = new ListNode();
node.val = val;
node.next = new ListNode();
```
23. Merge k Sorted Lists (*hard*)
> Convert to 'merge two lists' problem. Pairwisely merge two lists until one. Time complexity O(Nlogk).
206. Reverse linked list (*easy*)
> Use a temp node to record next node; change curr.next to the prev.
92. Reverse linked list II (*med*)
> Doing with a specific interval of the list.

## Two Pointers
```
Move pointers within the loop and update according to the conditions.
```
44. Wildcard Matching (hard0)
> Two pointers should be applied to base and pattern strings. 
> - In the loop, determine the match type: exact match, or star match.
> - maintain a sub pattern once star match met. 
> - The update of three pointers are very tricky. Can't present without testing.
125. Valid Palindrome (*easy*)
> Two pointers from start and end.

## Others
17. Letter Combinations of a Phone Number
316. Remove Duplicate Letters
- coding是一道简单题，given a list of integers, e.g. [1,5,3,8], 要求output一个list, [5x3x8, 1x3x8, 1x5x8, 5x3x8] 这个list 的第一个element 是given list 的除第一个element外其他三个element的product，第二个element是given list 的除第二个element外其他三个element的product， and so on.
```py
def solution (nums):
    mult = 1
    for item in nums: mult *= item
    result = []
    for i in range(len(nums)): result.append(mult / nums[i])
    return result
```
- 给一个word set, 里面包含了单词和短语（带有空格）。现在 从一个word stream 里面检测并输出在这个set里面有的词语和短语。这里稍微麻烦一点的是，word stream里面词语一个一个的来， 检测短语的时候需要特殊处理。
- design a data structure which supports two operations: Save phrases as the user send phrase to the server. Find all phrases that contain a list of keywords
- Write an English tokenizer
- 最后问的算法题是，给一个array作为input，返回它的variance。
- find longest subarray that sums to zero
- using uniform random generator to implement random sampling with probablity
- coding. Maze 题的变种。有些路径被block，但是不是整个cell被block，而是4个方向中有几个被block。找点A到点B的路径. 要求先设计data structure。然后再写algo 其实就是常规的BFS或者DFS，但是要按自己的data sturcture写code
- 528
- 寻找一个int array里面是否有(a^2+b^2=c^)； 基于本人完全没有好好刷过题，刚开始说出了brutal force的解决方案，解释了复杂度；然后小哥想让我optimize, 提示我一个sort，然后我边思考边说，给出了最佳解，完全不是背答案(因为真的不知道答案），是和小哥现场推演。
- 给定一个integer array，怎么判断一个target是不是在array里，不能用brute force。
- 一个多孩子tree，返回每一颗子树的height and size的ratio，一开始用bfs，后来发现错了，改用dfs应该没问题，又问了复杂度