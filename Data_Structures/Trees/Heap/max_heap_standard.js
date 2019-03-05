/* Standard implementation of a heap DS */

class MaxHeap {
    constructor() {
        this.heap = [];
        this.size = 0;
    }

    _parent(node) {
        return Math.floor((node - 1) / 2);
    }

    _swap(idx1, idx2) {
        var temp = this.heap[idx1];
        this.heap[idx1] = this.heap[idx2];
        this.heap[idx2] = temp;
    }

    insert(val) {
        this.heap.push(val);
        this.size++;

        var current = this.size;
        while (this.heap[current] > this.heap[this._parent(current)]) {
            this._swap(current, parent(current));
            current = parent(current);
        }
    }

    _isLeaf(pos) {
        if (pos >= ((this.size - 1) / 2) && pos <= this.size - 1) {
            return true;
        }
        return false;
    }

    leftChild(pos) {
        return (2 * pos) + 1;
    }

    rightChild(pos) {
        return (2 * pos) + 2;
    }

    _maxHeapify(pos) {
        if (this._isLeaf(pos)) {
            return;
        }
        var left = this.leftChild(pos);
        var right = this.rightChild(pos)
        if (this.heap[pos] < this.heap[left] || this.heap[pos] < this.heap[right]) {
            if (this.heap[left] > this.heap[right] || (!this.heap[right])) {
                this._swap(pos, left);
                this._maxHeapify(left);
            } else {
                this._swap(pos, right);
                this._maxHeapify(right);
            }
        }
    }

    // [100, 70, 30, 20, 10, 5, 1]
    extractMax() {
        this._swap(0, this.size - 1);
        var max = this.heap.pop();
        this.size--;
        this._maxHeapify(0);
        return max;
    }
}

var heap = new MaxHeap();
heap.insert(100);
heap.insert(70);
heap.insert(30);
heap.insert(40);
heap.insert(20);
heap.insert(10);

console.log(heap.heap);