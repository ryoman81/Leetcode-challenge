/**
 * Given a linked list, remove the n-th node from the end of list and return its head.
 * 
 * Example:
 * 
 * Given linked list: 1->2->3->4->5, and n = 2.
 * After removing the second node from the end, the linked list becomes 1->2->3->5.
 */

class ListNode {
    constructor (val, next) {
        this.val = (val===undefined ? 0 : val);
        this.next = (next===undefined ? null : next);
    }
}

var removeNthFromEnd = function(head, n) {
    const pointer_arr = [head];
    let pointer = head;
    while (pointer) {
        pointer_arr.push(pointer.next);         // [head, head.next, head.next.next, ..., null] length = linkedList.length + 1
        pointer = pointer.next;
    }
    
    const length = pointer_arr.length;
    if (n === length-1) {
        head = head.next;
    } else {
        pointer_arr[length-n-2].next = pointer_arr[length-n-2].next.next;
    }
    
    return head;
};