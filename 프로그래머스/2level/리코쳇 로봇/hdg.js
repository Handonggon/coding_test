const MOVE = [[0, -1], [-1, 0], [0, 1], [1, 0]];

function solution(board) {
    let [startY, startX] = [0, 0];
    for(let y = 0; y < board.length; y++) {
        for(let x = 0; x < board[y].length; x++) {
            if(board[y][x] === "R") {
                startY = y;
                startX = x;
            }
        }
    }
    let isMove = (y, x)=>(y >= 0 && y < board.length && x >= 0 && x < board[y].length && board[y][x] !== "D");
    let visited = Array.from(Array(board.length), (_, y)=>Array.from(Array(board[y].length), (_, x)=>Array(MOVE.length).fill(false)));

    let queue = [[startY, startX, 0]];
    while(queue.length) {
        let [y, x, c] = queue.shift();
        if(board[y][x] === "G") return c;
        
        for(let d = 0; d < MOVE.length; d++) {
            if(visited[y][x][d]) continue;
            visited[y][x][d] = true;
            let [dy, dx] = MOVE[d];
            for(let l = 1; isMove(y + (dy * l), x + (dx * l)); l++) {
                if(!isMove(y + (dy * (l + 1)), x + (dx * (l + 1)))) {
                    queue.push([y + (dy * l), x + (dx * l), c + 1]);
                }
            }
        }
    }
    return -1;
}