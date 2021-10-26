export default class Stack {
    constructor () {
        this.array = [];
    }

    peek () {
        return this.array[this.array.length-1];
    }

    pop () {
        this.array.pop();
        return this.array;
    }

    push (value) {
        this.array.push(value);
        return this.array;
    }

    size () {
        return this.array.length;
    }

    isEmpty () {
        return this.array.length === 0? true: false;
    }
}

const myStack = newStack();
myStack.push('Google');
myStack.push('Undemy');
myStack.push('Youtube');
myStack.peek();
myStack.pop();
myStack.pop();
myStack.pop();