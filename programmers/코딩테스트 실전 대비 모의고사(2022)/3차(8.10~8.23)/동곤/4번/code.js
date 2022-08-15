function solution(n, lighthouse) {
    let map = Array(n).fill().map(_=>[]);
    for(let [v, w] of lighthouse) {
        map[v-1].push(w-1);
        map[w-1].push(v-1);
    }

    function dfs(curr) {
        let [p, np] = [1, 0];
        for(let next of map[curr]) {
            if(curr > next) continue;
            let [cp, cnp] = dfs(next);
            [p, np] = [p + Math.min(cp, cnp), np + cp];
        }
        return [p, np];
    }
    return Math.min(...dfs(0));
}