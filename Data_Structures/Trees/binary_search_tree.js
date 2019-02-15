class Node {
    constructor(val) {
        this.val = val;
        this.left = null;
        this.right = null;
    }
}


class BST {
    constructor() {
        this.root = null
    }

    insert(val) {
        var newNode = new Node(val);
        if (!this.root) {
            this.root = newNode;
            return;
        }
        var current = this.root
        while (true) {
            if (current.val === val) return undefined
            if (current.val < val) {
                if (current.left === null) {
                    current.left = newNode;
                    return;
                }
                current = current.left
            }
            if (current.val > val) {
                if (current.right === null){
                    current.right = newNode;
                    return;
                }
                current = current.right
            }
        }
    }

    find(val) {
        var found = false;
        var current = this.root;

        while (this.current && !found) {
            if (current.val === val) {
                found = true
            }
            if (val < current.val) {
                current = current.left
            } else {
                current = current.right
            }
        }
        if (!found) {
            return undefined;
        };
        return current;
    }

    contains(val) {
        var found = false;
        var current = this.root;

        while (this.current && !found) {
            if (current.val === val) {
                found = true
            }
            if (val < current.val) {
                current = current.left
            } else {
                current = current.right
            }
        }
        return found;
    }
}

function breath_first_search(tree) {
    var queue = [];
    var visited = [];

    queue.push(tree.root)
    while (!queue.length) {
        elem = queue.shift();
        visited.push(elem)
        if (elem.left) {
            queue.push(elem.left)
        }
        if (elem.right) {
            queue.push(elem.right)
        }
    }
    return visited
}

//       8
//    4     10
//  2  5   9  11