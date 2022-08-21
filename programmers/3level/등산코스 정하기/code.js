function solution(n, paths, gates, summits) {
    const map = Array(n+1).fill().map(_=>Array(n+1).fill(Number.MAX_VALUE));
    for(let [i, j, w] of paths) {
        map[i][j] = w;
        map[j][i] = w;
    }
    
    summits = summits.reduce((newObj, obj) => {
        newObj[obj] = true;
        return newObj;
    }, {});
    
    let answer = [n+1, Number.MAX_VALUE];
    let visited = Array(n+1).fill().map((_, node)=>gates.includes(node));
    
    function dfs(curr, intensity) {
        if(summits[curr]) {
            if(answer[1] === intensity) {
                answer[0] = Math.min(answer[0], curr);
            } else {
                answer = [curr, intensity]
            }
        } else {
            for(let next = 1; next < map[curr].length; next++) {
                if(visited[next]) continue;
                if(map[curr][next] === Number.MAX_VALUE) continue;
                if(map[curr][next] > answer[1]) continue;
                    
                visited[next] = true;
                dfs(next, Math.max(intensity, map[curr][next]));
                visited[next] = false;
            }
        }
    }
    for(let gate of gates) {
        dfs(gate, 0);
    }
    return answer;
}