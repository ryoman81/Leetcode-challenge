export default class LinkedList {
    constructor (value) {
        // head follows the entire LL structure
        this.head = {
            value: value,
            next: null
        }
        // tail only follows the last node
        this.tail = this.head;
        this.length = 1;
    }

    append (value) {
        const newNode = {
            value: value,
            next: null
        }
        // because tail is a reference/pointer of previous node, update tail.next will update _previous.next
        this.tail.next = newNode;
        // then update the tail reference to a new node from the previous node
        this.tail = newNode;
        this.length++;
    }

    prepend (value) {
        const newNode = {
            value: value,
            next: null
        }
        newNode.next = this.head;
        // point this.head to the new structure
        this.head = newNode;
        this.length++;
    }

    insert (index, value) {
        // check valid indexing
        if (index >= this.length) {
            this.append(value);
            return;
        }
        if (index === 1) {
            this.prepend(value);
            return;
        }
        const newNode = {
            value: value,
            next: null
        }
        // In the following steps, we operate list through pointer
        let pointer = this.head;
        // Find the reference of left item
        for (let i = 0; i < index-1; i++) {
            pointer = pointer.next;   
        }
        // store a temp pointer to the right item
        const pointerTemp = pointer.next;
        // update right item with new node
        pointer.next = newNode;
        // concat temp right item to new node
        newNode.next = pointerTemp;

        this.length++;
    }

    remove (index) {
        if (index === 0) {
            this.head = this.head.next;
            this.length--;
            return;
        }
        if (index >= this.length) {
            return;
        }
        
        let pointer = this.head;
        for (let i = 0; i < index-1; i++) {
            pointer = pointer.next;
        }
        pointer.next = pointer.next.next;
        this.length--;
    }

    reverse () {
        if (this.length === 1) {
            return;
        }

        this.tail = this.head;

        let left = this.head;
        let middle = left.next;
        // loop over items and stop when right = null
        while (middle) {
            // store the right item 
            const right = middle.next;
            
            ////////////////////////////////////////////////////
            //    This is the core part: at each iteration,   // 
            //    we only CHANGE POINTER of current item      //
            //    from right to left.                         //
            ////////////////////////////////////////////////////
            middle.next = left;

            // Shift the center pointer //
            left = middle;
            middle = right;
        }

        // dealing with the last item since we stopped at null
        this.head.next = null;
        this.head = left;
    }


    printList () {
        const array = [];
        let currentNode = this.head;
        while (currentNode !== null) {
            array.push(currentNode.value);
            currentNode = currentNode.next;
        }
        console.log(array, this.length);
    }
}

const myLinkedList = new LinkedList(10);
myLinkedList.append(5);
myLinkedList.append(16);
myLinkedList.prepend(1);
myLinkedList.insert(2, 99);
myLinkedList.insert(20, 88);
myLinkedList.printList();
myLinkedList.remove(2);
myLinkedList.printList();
myLinkedList.reverse();
myLinkedList.printList();