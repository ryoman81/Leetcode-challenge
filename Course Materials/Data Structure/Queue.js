class Node {
    constructor (value) {
        this.value = value;
        this.next = null;
    }
}

export default class Queue {
    constructor () {
        this.first = null;  // link list head
        this.last = null;   // link list tail
        this.length = 0;
    }

    peek () {
        return this.first;
    }

    enqueue (value) {
        const newNode = new Node(value);
        // To understand this part, this.first and this.last only are pointers
        // that point to a specific region of memory space
        // Once initiates them, they are both pointing to a space created by newNode
        if (this.length === 0) {
            this.first = newNode;
            this.last = newNode;
        } else {
            this.last.next = newNode;
            this.last = newNode;
        }
        this.length++;
    }

    dequeue () {
        if (this.length === 0) {
            return;
        }
        if (this.first === this.last) {
            this.last = null;
        }
        // in JS, if there is no pointer pointing to a memory space, 
        // that data will garbage collected
        this.first = this.first.next;
        this.length--;
    }
}

const myQueue = new Queue();
myQueue.peek();
myQueue.enqueue('Joy');
myQueue.enqueue('Matt');
myQueue.enqueue('Pavel');
myQueue.enqueue('Samir');
myQueue.dequeue();
myQueue.dequeue();
myQueue.dequeue();
