function solution(n, lighthouse) {
    let answer = 0;
    const visited = new Array(n + 1).fill(false);
    while(lighthouse.length) {
        let graph = Array.from(Array(n + 1), () => new Array());
        for(let [u, v] of lighthouse) {
            graph[u].push(v);
            graph[v].push(u);
        }
        for(let [target] of graph.filter(curr=>curr.length === 1)) {
            if(visited[target]) continue;
            visited[target] = true;
            if(graph[target].length === 1) {
                answer += 0.5;
            } else {
                answer += 1;
            }
        }
        lighthouse = lighthouse.filter(([u, v])=>(!visited[u] && !visited[v]));
    }
    return answer;
}