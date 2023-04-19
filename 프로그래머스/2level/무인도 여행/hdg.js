const MOVE = [[0, -1], [-1, 0], [0, 1], [1, 0]];

function solution(maps) {
    let answer = [];
    
    let isMove = (y, x)=>(y >= 0 && y < maps.length && x >= 0 && x < maps[y].length);
    let visited = Array.from(Array(maps.length), (_, y)=>Array(maps[y].length).fill(false));
    for(let i = 0; i < maps.length; i++) {
        for(let j = 0; j < maps[i].length; j++) {
            let day = 0;
            let stack = [[i, j]];
            while(stack.length) {
                let [y, x] = stack.pop();
                if(visited[y][x] || maps[y][x] === 'X') continue;
                visited[y][x] = true;
                day += +maps[y][x];
                
                for(let [dy, dx] of MOVE) {
                    if(isMove(dy + y, dx + x)) stack.push([dy + y, dx + x]);
                }
            }
            answer.push(day);
        }
    }
    return answer.every(day=>day===0) ? [-1] : answer.filter(day=>day!==0).sort((a, b)=>a-b);
}