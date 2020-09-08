class LinkedList {
    constructor (value) {
        // head follows the entire LL structure
        this.head = {
            value: value,
            next: null,
            prev: null
        }
        // tail only follows the last node
        this.tail = this.head;
        this.length = 1;
    }

    append (value) {
        const newNode = {
            value: value,
            next: null,
            prev: null
        }
        newNode.prev = this.tail;
        // because tail is a reference/pointer of previous node, update tail.next will update _previous.next
        this.tail.next = newNode;
        // then update the tail reference to a new node from the previous node
        this.tail = newNode;
        this.length++;
    }

    prepend (value) {
        const newNode = {
            value: value,
            next: null,
            prev: null
        }
        newNode.next = this.head;
        // point this.head to the new structure
        this.head.prev = newNode;
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
            next: null,
            prev: null
        }
        // In the following steps, we operate list through pointer
        let pointer_left = this.head;
        let pointer_right = this.head.next;
        // Find the reference of left item
        for (let i = 0; i < index-1; i++) {
            pointer_left = pointer_left.next; 
            pointer_right = pointer_left.next;
        }
    
        pointer_left.next = newNode;
        newNode.prev = pointer_left;
        newNode.next = pointer_right;
        pointer_right.prev = newNode;

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
        
        let pointer_left = this.head;
        for (let i = 0; i < index-1; i++) {
            pointer_left = pointer_left.next;
        }
        pointer_left.next = pointer_left.next.next;
        pointer_left.next.prev = pointer_left;
        this.length--;
    }

    printList () {
        const array = [];
        let currentNode = this.head;
        while (currentNode !== null) {
            array.push(currentNode.value);
            currentNode = currentNode.next;
        }
        console.log(array);
    }
}

const myLinkedList = new LinkedList(10);
myLinkedList.append(5);
myLinkedList.append(16);
myLinkedList.prepend(1);
myLinkedList.insert(2, 99);
myLinkedList.insert(20, 88);
myLinkedList.remove(3);
myLinkedList.printList();