const MOVE = [[0, -1], [-1, 0], [0, 1], [1, 0]];
const INF = 100 * 100;

function solution(maps) {
    let isMove = (y, x)=>(0 <= y && y < maps.length && 0 <= x && x < maps[y].length && maps[y][x] !== "X");
    let location = {};
    for(let i = 0; i < maps.length; i++) {
        for(let j = 0; j < maps[i].length; j++) {
            location[maps[i][j]] = [i, j];
        }
    }
    
    function find(orgin, target) {
        let visited = Array.from(Array(maps.length), ()=>Array(maps.length).fill(false));
        let queue = [[...location[orgin], 0]];
        
        while(queue.length) {
            let [y, x, count] = queue.shift();
            if(maps[y][x] === target) return count;
            if(visited[y][x]) continue;
            visited[y][x] = true;

            for(let [dy, dx] of MOVE) {
                if(isMove(y + dy, x + dx)) {
                    queue.push([y + dy, x + dx, count + 1]);
                }
            }
        }
        return INF;
    }
    let answer = find("S", "L") + find("L", "E");
    return answer >= INF ? -1 : answer;
}