class Heap {
    constructor() {
        this.data = [];
    }

    heapify() {
        var idx = this.data.length - 1;
        var parent = Math.floor((idx - 1) / 2);
        while (this.data[idx] > this.data[parent] && parent >= 0) {
            var temp = this.data[idx];
            this.data[idx] = this.data[parent];
            this.data[parent] = temp;
            idx = parent;
            parent = Math.floor((idx - 1) / 2);
        }
    }

    insert(val) {
        this.data.push(val);
        if (this.data.length === 1) {
            return;
        }
        this.heapify()
    }
}

var heap = new Heap();
heap.insert(100);
heap.insert(70);
heap.insert(30);
heap.insert(40);
heap.insert(20);
heap.insert(10);

heap.extractMax()
//            110
//        80      100
//    70     20   10  30
//   5 40
//
// [100, 70, 30, 40, 20, 10]
// [100, 70, 80, 40, 20, 10, 30]

// [110, 70, 100, 40, 20, 10, 30]
// 110, 80, 100, 70, 20, 10, 30, 5, 40]