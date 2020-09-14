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
    
    while (true) {
        sum = carry;
        if (l1) {
            sum += l1.val;
        }
        if (l2) {
            sum += l2.val;
        }
        
        if (sum < 10) {
            carry = 0;
        } else {
            carry = 1;
            sum = sum - 10;
        }
        pointer.val = sum;
        
        // if l1 l2 have next
        if (l1.next || l2.next) {
            pointer.next = new ListNode();
            pointer = pointer.next;
            if (!l1.next) {
                l1 = 0;
                l2 = l2.next;
                continue;
            }
            if (!l2.next) {
                l1 = l1.next;
                l2 = 0;
                continue;
            }
            l1 = l1.next;
            l2 = l2.next;
        // if l1 l2 end but has a carry
        } else if (carry) {
            pointer.next = new ListNode(1);
            break;
        // if l1 l2 end and has no carry
        } else {
            break;
        }
    }
    
    return head;
};