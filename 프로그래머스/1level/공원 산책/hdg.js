let MOVE = {N: [-1, 0], S: [1, 0], W: [0, -1], E: [0, 1]};

function solution(park, routes) {
    let [y, x] = [0, 0];
    for(let i = 0; i < park.length; i++) {
        for(let j = 0; j < park[i].length; j++) {
            if(park[i][j] === "S") [y, x] = [i, j];
        }
    }
    
    let isMove = (y, x)=>(y >= 0 && y < park.length && x >= 0 && x < park[y].length && park[y][x] !== "X");
    
    for(let [dir, len] of routes.map(route=>route.split(" "))) {
        let [dy, dx] = MOVE[dir];
        if([...Array(Number(len) + 1).keys()].map(l=>[dy * l, dx * l])
           .every(([dy, dx])=>isMove(y + dy, x + dx))) {
            y += dy * len;
            x += dx * len;
        }
    }
    return [y, x];
}