let MOVE = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]];

function solution(board, y, x) {
    board = board.map(y=>y.split(''));

    //지뢰가 없는 경우
    if(board[y][x] === 'E') {
        function isBound(my, mx) {
            return my >= 0 && my < board.length && mx >= 0 && mx < board[my].length;
        }
        
        let visited = Array(board.length).fill(0).map((_, y)=>Array(board[y].length).fill('E'));
        /*
        function dfs(my, mx) {
            let count = 0;
            for(let move of MOVE) {
                let [dy, dx] = move;
                if(isBound(my+dy, mx+dx)) {
                    if(board[my+dy][mx+dx] === 'M') count += 1;
                    else if(board[my+dy][mx+dx] === 'E') {
                        count += dfs(my+dy, mx+dx);
                    } else {
                        count += board[my+dy][mx+dx];
                    }
                }
            }
            visited[my][mx] = count;
            return count;
        }
        dfs(y, x);
        */
        let queue = [];
        queue.push([y, x]);
        while(queue.length) {
            let [my, mx] = queue.shift();
            if(visited[my][mx] === 'E') {
                let count = 0;
                for(let move of MOVE) {
                    let [dy, dx] = move;
                    if(isBound(my+dy, mx+dx)) {
                        if(board[my+dy][mx+dx] === 'M') count++;
                    }
                }
                visited[my][mx] = (count === 0) ? 'B' : count;

                if(count === 0) {
                    for(let move of MOVE) {
                        let [dy, dx] = move;
                        if(isBound(my+dy, mx+dx) && visited[my+dy][mx+dx] === 'E') {
                            queue.push([my+dy, mx+dx]);
                        }
                    }
                }
            }
        }
        board = visited;
    } 
    //지뢰가 있는 경우
    else {
        board[y][x] = 'X';
    }
    return board.map(y=>y.join(''));
}