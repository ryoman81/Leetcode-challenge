/**
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
 */

class ListNode {
    constructor (val, next) {
        this.val = (val===undefined ? 0 : val);
        this.next = (next===undefined ? null : next);
    }
}

const addTwoNumbers = function (l1, l2) {
    const head = new ListNode(0);
    let pointer = head;
    let sum = 0;
    let carry = 0;
    
    while (l1 || l2 || carry) {
        sum = carry;
        if (l1) {
            sum += l1.val;
            l1 = l1.next;
        }
        if (l2) {
            sum += l2.val;
            l2 = l2.next;
        }
        
        if (sum < 10) {
            carry = 0;
        } else {
            carry = 1;
            sum = sum - 10;
        }
        pointer.next = new ListNode(sum);
        pointer = pointer.next;
    }
    
    return head.next;
};