class Node {
    constructor(val) {
        this.val = val;
        this.left = null;
        this.right = null;
    }
}

class BST {
    constructor() {
        this.root = null;
    }

    insert(val) {
        var newNode = new Node(val);
        if (!this.root) {
            this.root = newNode;
            return;
        }

        var current = this.root;
        while (true) {
            if (val < current.val) {
                if (current.left === null) {
                    current.left = newNode;
                    return;
                }
                current = current.left;
            }
            if (val > current.val) {
                if (current.right === null) {
                    current.right = newNode;
                    return;
                }
                current = current.right;
            }
        }
    }
}

//       8
//    4     10
//  2  5   9  11

// s = [8]
// [8, 4, 2]

function inorder(tree) {
    var current = tree.root;
    var result = [];
    var done = false;
    var stack = [];

    while(!done) {
        // Traverse all the nodes in the left
        // append it to the stack
        if (current !== null) {
            stack.push(current);
            current = current.left;
        } else {
            if (stack.length > 0) {
                 current = stack.pop();
                 result.push(current.val);
                 current = current.right;       
            } else {
                done = true;
            }
        }
    }
    return result;
}

var tree = new BST()
tree.insert(8)
tree.insert(4)
tree.insert(2)
tree.insert(5)
tree.insert(10)
tree.insert(9)
tree.insert(11)

console.log(inorder(tree));