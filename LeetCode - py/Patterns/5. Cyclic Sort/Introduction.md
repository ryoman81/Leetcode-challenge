# Pattern: Cyclic Sort, 循环排序
这种模式讲述的是一直很好玩的方法：可以用来处理数组中的数值限定在一定的区间的问题。这种模式一个个遍历数组中的元素，如果当前这个数它不在其应该在的位置的话，就把它和它应该在的那个位置上的数交换一下。

<img src="https://pic2.zhimg.com/80/v2-e5a2fe3faa0b55ad5c6d8f182039cd35_1440w.jpg?source=1940ef5c" />

这些问题一般设计到**排序好的数组**，而且**数值一般满足于一定的区间**
- 如果问题让你需要在排好序/翻转过的数组
- 寻找丢失的/重复的/最小的元素

## **解题思路:**
根据总结, 如果简单题目当中对array和index提出一些条件, 包array[i]在某个范围[0,n] or [1,n]时, 如果问题提及一些, find missing, find minimum, find duplicate... 则可以使用cyclic sort方法解之. 大体思路则是, 把数 x=nums[i] 放在位置 index=x 或者左右某处的地方. 最后再来个循环, 检测是否index=x的位置上是否有 x 这个值或者相关的值存在. 满足一定条件之后, 需要做的是交换 nums[i] 和 nums[crr]或周围 的元素.

## **经典题目:**

- 41. First Missing Positive (hard)
- 268. Missing Number (easy)
- 287. Find the duplicate Number (med)
- 442. Find all Duplicates in an Array (med)
- 448. Find All Numbers Disappeared in an Array (easy)
- 765. Couples Holding Hands (hard)

## **参考链接 Reference:**

- https://blog.techbridge.cc/2020/02/16/leetcode-%E5%88%B7%E9%A1%8C-pattern-cyclic-sort/ 

## **模板 Template:**
The template pattern is very suitable and consistant in the similar problems
### **Python**
```py
def cyclicSort (nums):
  # start the index at the first for the while-loop
  i = 0
  # while out all members in the nums array
  while i < len(nums):
    # varible the current value
    crr = nums[i]

    # Conditioning to check:
    # if crr is negative/positive as the requirement in the problem?
    # if crr is out the indexing boundary?
    # (key) if crr is same or not to the desitinate position?
    if (crr...):
      # if applied, then we do swap in place of array
      # be careful of the indexing. Many times, the range is [1, len+1]
      # using Python3 assignment syntax to swap
      nums[i], nums[crr] = nums[crr], nums[i]
    else:
      # if not apply or need to skip this element, then we increment this i index
      i += 1

  # After while-loop we usually do a value-index check process
  for i in range(len(nums)):
    if nums[i] != i:    # be mindful about the indexing and position
      return i

  # sometime we need to return sometime if the previous while-loop check succeeded for all members
  return len(nums)
```

### **JavaScript**
```js
const cyclicSort (nums) => {
  // while out all members in the nums array
  while (let i < len(nums)) {
    // varible the current value
    const crr = nums[i]

    // Conditioning to check:
    // if crr is negative/positive as the requirement in the problem? [crr > 0?]
    // if crr is out the indexing boundary? [crr > nums.length?]
    // (key) if crr is same or not to the desitinate position? [crr === nums[crr]?]
    if (crr...) {
      // if applied, then we do swap in place of array
      // be careful of the indexing. Many times, the range is [1, len+1]
      // in JavaScript, there is ES6 destructuring assignment to swap two elements in array
      [nums[i], nums[crr]] = [nums[crr], nums[i]];
    } else {
      // if not apply or need to skip this element, then we increment this i index
      i++;
    }
  }
  // After while-loop we usually do a value-index check process
  for (let i = 0; i <nums.length; i++) {
    if (nums[i] !== i)    # be mindful about the indexing and position
      return i;
  }
  // sometime we need to return sometime if the previous while-loop check succeeded for all members
  return len(nums);
}
```