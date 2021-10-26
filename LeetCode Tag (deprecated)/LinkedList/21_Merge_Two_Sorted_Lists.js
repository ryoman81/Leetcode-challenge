/**
 * Merge two sorted linked lists and return it as a new sorted list. 
 * The new list should be made by splicing together the nodes of the first two lists.
 * 
 * Example:
 * 
 * Input: 1->2->4, 1->3->4
 * Output: 1->1->2->3->4->4
 */

class ListNode {
    constructor (val, next) {
        this.val = (val===undefined ? 0 : val);
        this.next = (next===undefined ? null : next);
    }
}

var mergeTwoLists = function(l1, l2) {
    const head = new ListNode(0);
    let pointer = head;
    while (l1 && l2) {
        if (l1.val < l2.val) {
            pointer.next = new ListNode(l1.val);
            pointer = pointer.next;
            l1 = l1.next;
            
        } else {
            pointer.next = new ListNode(l2.val);
            pointer = pointer.next;
            l2 = l2.next;
        }
    }
        
    
    while (l1) {
        pointer.next = new ListNode(l1.val);
        pointer = pointer.next;
        l1 = l1.next;
    }
    
    while (l2) {
        pointer.next = new ListNode(l2.val);
        pointer = pointer.next;
        l2 = l2.next;
    }
    
    return head.next;
};