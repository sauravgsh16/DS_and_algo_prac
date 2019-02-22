/* Implementation of a hash table, using chaining to avoid collisions */

class HashMap {
    constructor(size = 53) {
        this.hashmap = new Array(size);
    }

    _hash(key) {
        let total = 0;
        let WEIRD_PRIME = 53;
        for (var i = 0; i < Math.min(key.length, 100); i++) {
            var char = key[i];
            let val = char.charCodeAt(0) - 96;
            total = (total * WEIRD_PRIME + val) % this.hashmap.length;
        }
        return total;
    }

    set(key, value) {
        var idx = this._hash(key);
        if (!this.hashmap[idx]) {
            this.hashmap[idx] = [];
        }
        this.hashmap[idx].push([key, value]);
    }

    get(key) {
        var idx = this._hash(key);
        if (this.hashmap[idx]) {
            for (var i = 0; i < this.hashmap[idx].length; i++) {
                if (this.hashmap[idx][i][0] === key) {
                    return this.hashmap[idx][i][1];
                }
            }
        }
        return undefined;
    }
}

var hash = new HashMap();