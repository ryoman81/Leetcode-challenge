# Pattern: Merge Intervals, 区间合并类型

<img src="https://pic4.zhimg.com/80/v2-29f25eef886240f3ed3767039fb8f1db_720w.jpg?source=1940ef5c" />

## **解题思路:**

Binary Search 是一类模板性很强的题目, 以**模板优先**. 二分查找法的前置条件要拥有一个已经Sorted好的序列, 这样在查找所要查找的元素时首先与序列中间的元素进行比较, 如果大于这个元素就在当前序列的后半部分继续查找, 如果小于这个元素就在当前序列的前半部分继续查找, 直到找到相同的元素或者所查找的序列范围为空为止.

但是BS当中有很多容易出现的隐性bugs包括两点
1. 溢出: 有可能 left+right 超出整型边界, 可以将
    ```
    mid = (left + right) // 2
    ```
    变为
    ```
    mid = left + (right - left) // 2
    ```
2. 边界错误: 我们用的模板是左闭右闭 [left, right], 也有的模板用的左闭右开 [left, right). 不同情况下在while循环里面的条件判断要写准确 < 或者 <=, 以免造成越界或者死循环.

题目类型分为
1. 有target: 要求你找一个Target值一般找到就返回Target值的下标或者Boolean函数
2. 无target: 这一类的题比较多变可能会要你找
   - 比Target大的最小值
   - 比Target小的最大值
   - 满足要求的第一个值
   - 不满足要求的最后一个值
<img src="https://raw.githubusercontent.com/yuzhoujr/leetcode/master/img/binary_search.png" />

## **经典题目:**

- 33. Search in rotated sorted array (med)
- 34. Search for a range (easy)
- 74. Search a 2D matrix (med)
- 81. Search in rotated sorted array II (med)
- 153. Find minimum in rotated sorted array (med)
- 240. Search a 2D matrix II (med)
- 278. First bad version (easy)
- 658. Find K closest elements (med)

**Other listed by the reference**

- 4 33 74 240
- 33 74 81 153 162 704 744
- 33 34 367 374 458
- 29 33 34 74 81 153 209 222 230 240 278 287 300 378 436 454 658 718
- 33 34 35 74 81 153 154 162 230 240 275 278 287 349 350 367 378 441 658 744

## **参考链接 Reference:**

- https://www.1point3acres.com/bbs/thread-432793-1-1.html
- https://zhuanlan.zhihu.com/p/137625540
- https://www.jianshu.com/p/e090b298e36d
- https://zxth93.github.io/2017/11/20/LeetCode-binary-search%E7%B1%BB%E6%80%BB%E7%BB%93/index.html 

## **模板 Template:**
### **Python**
```py
def binarySearch (arr, target):
  # Initialize left and right pointers
  # Prefer a double closure form that covers the last index 
  left = 0
  right = len(arr) - 1

  # The main while-loop. noted the equal sign <=
  while left <= right:
    # find the middle pointer
    mid = (left + right) // 2   # '//' in Python returns FLOOR integer after division
    
    # condition of target found
    if arr[mid] == target: 
      return mid
    
    # move to the right part
    if target > arr[mid]:
      left = mid + 1
    # move to the left part  
    else: 
      right = mid - 1

  # if no result return -1 or else
  return -1
```

### **JavaScript**
```js
function binarySearch (arr, target) {
  // Initialize left and right pointers
  // Prefer a double closure form that covers the last index 
  let left = 0;
  let right = arr.length - 1;

  // The main while-loop. noted the equal sign <=
  while (left <= right) {
    // find the middle pointer
    let mid = Math.floor((left+right)/2);   // Please use some genious way in JS 
    
    // condition of target found
    if (target === arr[mid])
        return mid;

    // move to the right part
    if (target > arr[mid]) {
        left = mid + 1;
    // move to the left part      
    } else {
        right = mid - 1;
    }        
  }
  // if no result return -1 or else
  return -1;
}
```