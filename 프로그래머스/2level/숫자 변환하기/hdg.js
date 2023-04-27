function solution(x, y, n) {
    let way = [(v)=>v + n, (v)=>v * 2, (v)=>v * 3];
    
    let dp = Array(y + 1).fill(y);
    dp[x] = 0;
    for(let curr = x; curr < y; curr++) {
        for(let next of way.map(fn=>fn(curr))) {
            if(next > y) continue;
            dp[next] = Math.min(dp[next], dp[curr] + 1);
        }
    }
    return dp[y] === y ? -1 : dp[y];
}