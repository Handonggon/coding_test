const MOVE = [[1, 0, 'd'], [0, -1, 'l'], [0, 1, 'r'], [-1, 0, 'u']];

function solution(n, m, x, y, r, c, k) {
    let isBoundary = (x, y)=>(1 <= x && x <= n && 1 <= y && y <= m);
    let getDist = (x, y)=>(Math.abs(r - x) + Math.abs(c - y));

    let queue = [[x, y, ""]];
    while(queue.length) {
        let [x, y, t] = queue.shift();
        if(x === r && y === c && (k - t.length) % 2 === 1) return "impossible";
        if(x === r && y === c && t.length === k) return t;

        for(let [dx, dy, dt] of MOVE) {
            if(isBoundary(x + dx, y + dy) && getDist(x + dx, y + dy) + t.length + 1 <= k) {
                queue.push([x + dx, y + dy, t + dt]);
                break;
            }
        }
    }
    return "impossible";
}