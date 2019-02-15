class Node {
    constructor(val) {
        this.val = val;
        this.left = null;
        this.right = null
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


// Inorder traversal
function inOrder(tree) {
    var result = [];
    function traverse(node) {
        if (node !== null) {
            traverse(node.left);
            result.push(node.val);
            traverse(node.right);
        }
    }
    traverse(tree.root);
    return result;
}

function preOrder(tree) {
    var result = [];
    function traverse(node) {
        if (node !== null) {
            result.push(node.val);
            traverse(node.left);
            traverse(node.right);
        }
    }
    traverse(tree.root);
    return result;
}

function postOrder(tree) {
    var result = [];
    function traverse(node) {
        if (node !== null) {
            traverse(node.left);
            traverse(node.right);
            result.push(node.val);
        }
    }
    traverse(tree.root);
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

//       8
//    4     10
//  2  5   9  11

// s = [8]
// [8, 4, 2]

console.log(inOrder(tree));
console.log(preOrder(tree));
console.log(postOrder(tree));