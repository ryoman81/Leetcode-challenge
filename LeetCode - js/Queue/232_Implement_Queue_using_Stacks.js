/**Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty. */


/**
 * Initialize your data structure here.
 */
class Stack {
    constructor () {
        this.array = [];
    }
    peek () {
        return this.array[this.array.length-1];
    }
    pop () {
        return this.array.pop();
    }
    push (value) {
        this.array.push(value);
    }
    size () {
        return this.array.length;
    }
    isEmpty () {
        return this.array.length === 0? true: false;
    }
}

class MyQueue {
    constructor () {
        this.stack = new Stack();
    }
    
    /**
     * Push element x to the back of queue. 
     * @param {number} x
     * @return {void}
     */
    push (x) {
        const tempStack = [];
        while (this.stack.size()) {
            tempStack.push(this.stack.pop());
        }
        tempStack.push(x);
        while (tempStack.length) {
            this.stack.push(tempStack.pop());
        }
    };

    /**
     * Removes the element from in front of queue and returns that element.
     * @return {number}
     */
    pop () {
        return this.stack.pop();
    };

    /**
     * Get the front element.
     * @return {number}
     */
    peek () {
        return this.stack.peek();
    };

    /**
     * Returns whether the queue is empty.
     * @return {boolean}
     */
    empty () {
        return this.stack.isEmpty();
    };   
}

/** 
 * Your MyQueue object will be instantiated and called as such:
 * var obj = new MyQueue()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.empty()
 */
const obj = new MyQueue();
obj.push(1);
obj.push(2);
obj.push(3);

console.log(obj.pop());
console.log(obj.peek());
console.log(obj.empty());