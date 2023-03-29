function solution(n, roads, sources, destination) {
    let adj = Array.from(Array(n + 1), ()=>[]);
    for(let [u, v] of roads) {
        adj[u].push(v);
        adj[v].push(u);
    }
    let costs = Array(n + 1).fill(-1);
    costs[destination] = 0;
    let queue = [destination];
    while(queue.length) {
        let curr = queue.shift();
        for(let next of adj[curr]) {
            if(costs[next] > -1) continue;
            queue.push(next);
            costs[next] = costs[curr] + 1;
        }
    }
    return sources.map(source=>costs[source]);
}