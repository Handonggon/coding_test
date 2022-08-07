const INFINITY = 100001;

function solution(n, roads, sources, destination) {
    const map = Array(n).fill().map(_=>Array());
    for(let [curr, next] of roads) {
        map[curr-1].push(next-1);
        map[next-1].push(curr-1);
    }
    let dist = dijkstra(destination-1, map);
    return sources.map(source=>dist[source-1])
                  .map(source=>source===INFINITY?-1:source);
}

class Node {
    constructor(number, distance) {
        this.number = number;
        this.distance = distance;
    }
}

class Heap {
    constructor() {
        this.heap = [];
    }
    push(newValue) {
        const heap = this.heap;
        heap.push(newValue);
        let index = heap.length - 1;
        let parent = Math.floor((index - 1) / 2);
        while(index > 0 && heap[parent].distance > heap[index].distance) {
            [heap[parent], heap[index]] = [heap[index], heap[parent]];
            index = parent;
            parent = Math.floor((index - 1) / 2);
        }
    }
    pop() {
        const heap = this.heap;
        if(heap.length <= 1) return heap.pop();
        const ret = heap[0];
        heap[0] = heap.pop();
        let here = 0;
        while(1) {
            let left = here * 2 + 1, right = here * 2 + 2;
            if(left >= heap.length) break;
            let next = here;
            if (heap[next].distance > heap[left].distance) next = left;
            if (right < heap.length && heap[next].distance > heap[right].distance) next = right;
            if (next === here) break;
            [heap[here], heap[next]] = [heap[next], heap[here]];
            here = next;
        }
        return ret;
    }
    length() {
        return this.heap.length;
    }
}

function dijkstra(start, map) {
    const dist = Array(map.length).fill(INFINITY);
    dist[start] = 0;
    
    const pq = new Heap();
    pq.push(new Node(start, 0));
    
    while(pq.length()) {
        let node = pq.pop();
        
        if(node.distance > dist[node.number]) continue;
        
        for(let next of map[node.number]) {
            if(dist[next] > node.distance + 1) {
                dist[next] = node.distance + 1;
                pq.push(new Node(next, node.distance + 1));
            }
        }
    }
    return dist;
}