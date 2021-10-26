class Node {
    constructor (value) {
        this.left = null;
        this.right = null;
        this.value = value;
    }
}

class BinarySearchTree {
    constructor () {
        this.root = null;
    }

    lookup (value) {
        if (!this.root) return false;

        let pointer = this.root;
        while (true) {
            if (value === pointer.value) {
                return true;
            } else if (value < pointer.value) {
                pointer = pointer.left;
            } else {
                pointer = pointer.right;
            }

            if (!pointer) return false;
        }

    }

    insert (value) {
        const newNode = new Node(value);
        if (!this.root) {
            this.root = newNode;
            return;
        }
        let pointer = this.root;
        while (true) {
            if (value < pointer.value) {
                if (!pointer.left) {
                    pointer.left = newNode;
                    return;
                }
                pointer = pointer.left;
            } else {
                if (!pointer.right) {
                    pointer.right = newNode;
                    return;
                }
                pointer = pointer.right;
            }
        }
    }

    remove (value) {
        if (!this.root) {
            return false;
        }
        let currentNode = this.root;
        let parentNode = null;
        while (currentNode) {
            if (value < currentNode.value) {
                parentNode = currentNode;
                currentNode = currentNode.left;
            } else if (value > currentNode.value) {
                parentNode = currentNode;
                currentNode = currentNode.right;
            // if we match, we shall divide to three scenarios
            } else {
                // Option 1: no right child
                if (currentNode.right === null) {
                    if (parentNode === null) {
                        this.root = currentNode.left;
                    } else {
                        if (currentNode.value < parentNode.value) {
                            parentNode.left = currentNode.left;
                        } else {
                            parentNode.right = currentNode.left;
                        }
                    }
                }
                // Option 2: has right child, but the right child has no left child
                else if (currentNode.right.left === null) {
                    if (parentNode === null) {
                        this.root = currentNode.left;
                    } else {
                        currentNode.right.left = currentNode.left;
                        if (currentNode.value < parentNode.value) {
                            parentNode.left = currentNode.right;
                        } else {
                            parentNode.right = currentNode.right;
                        }
                    }
                //Option 3: Right child that has a left child
                } else {

                    //find the Right child's left most child
                    let leftmost = currentNode.right.left;
                    let leftmostParent = currentNode.right;
                    while(leftmost.left !== null) {
                        leftmostParent = leftmost;
                        leftmost = leftmost.left;
                    }
            
                    //Parent's left subtree is now leftmost's right subtree
                    leftmostParent.left = leftmost.right;
                    leftmost.left = currentNode.left;
                    leftmost.right = currentNode.right;
  
                    if(parentNode === null) {
                        this.root = leftmost;
                    } else {
                        if(currentNode.value < parentNode.value) {
                            parentNode.left = leftmost;
                        } else if(currentNode.value > parentNode.value) {
                            parentNode.right = leftmost;
                        }
                    }
                }
                return true;
            }
        }
    }

    BFSItr() {
        // use a list array to record the BFS result
        const list = [];
        // use a queue to keep tracking the BFS node
        // this queue can be pretty large as for keeping reference of nodes
        const queue = [];
        // let the current node starts from root
        let currentNode = this.root;
        
        queue.push(currentNode);
        while (queue.length > 0) {
            // remove and return the first item in the queue
            currentNode = queue.shift();
            // record the value of current node
            list.push(currentNode.value);
            // check the current node if has left and right child
            if (currentNode.left)
                queue.push(currentNode.left);
            if (currentNode.right)
                queue.push(currentNode.right);
        }

        return list;
    }

    BFSRec (queue, list) {
        if (!queue.length) {
            return list;
        }
        let currentNode = queue.shift();
        list.push(currentNode.value);
        if (currentNode.left)
            queue.push(currentNode.left);
        if (currentNode.right)
            queue.push(currentNode.right);
        return this.BFSRec(queue,list);
    }

    DFS (type) {
        // the key of DFS implementation is to recursively get deep until left or right to be null
        // what makes different is the order to push in the value
        switch (type) {
            case "inOrder":
                return in_order (this.root, []);
            case "preOrder":
                return pre_order (this.root, []);
            case "postOrder":
                return post_order (this.root, []);
            default:
                return false;
        }

        function in_order (node, list) {
            // to go all the way down to the end left child
            if (node.left)
                in_order(node.left, list);
            // going back to the parent
            list.push(node.value);
            // search the right child 
            if (node.right)
                in_order(node.right, list);
            return list;
        }

        function pre_order (node, list) {
            // push the current value first
            list.push(node.value);
            // to go all the way down to the end left child
            if (node.left)
                pre_order(node.left, list);
            // search the right child 
            if (node.right)
                pre_order(node.right, list);
            return list;
        }

        function post_order (node, list) {
            // to go all the way down to the end left child
            if (node.left)
                post_order(node.left, list);
            // search the right child 
            if (node.right)
                post_order(node.right, list);
            // push the current value
            list.push(node.value);
            return list;
        }
    }
}

//      9
//  4       20
//1   6  15   170
const tree = new BinarySearchTree ();
tree.insert(9);
tree.insert(4);
tree.insert(6);
tree.insert(20);
tree.insert(170);
tree.insert(15);
tree.insert(1);

console.log(tree.BFSItr());
console.log(tree.BFSRec([tree.root], []));
console.log(tree.DFS("inOrder"));
console.log(tree.DFS("preOrder"));
console.log(tree.DFS("postOrder"));