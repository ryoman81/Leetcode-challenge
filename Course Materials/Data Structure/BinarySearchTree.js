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
}

traverse_tree = (node) => {
    const tree = {value: node.value};
    tree.left = node.left === null? null:
    traverse_tree(node.left);
    tree.right = node.right === null? null:
    traverse_tree(node.right);
    return tree;
}

const tree = new BinarySearchTree ();
tree.insert(9);
tree.insert(4);
tree.insert(6);
tree.insert(20);
tree.insert(170);
tree.insert(15);
tree.insert(1);
//      9
//  4       20
//1   6  15   170
console.log(JSON.stringify(traverse_tree(tree.root)));

console.log(tree.lookup(9));
console.log(tree.lookup(20));
console.log(tree.lookup(191));

tree.remove(4);
console.log(JSON.stringify(traverse_tree(tree.root)));