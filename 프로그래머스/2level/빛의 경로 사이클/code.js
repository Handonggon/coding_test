const TYPE = ["U", "D", "L", "R"];
const MOVE = {S:(type)=>[[-1,  0, 0], [ 1,  0, 1], [ 0, -1, 2], [ 0,  1, 3]][type]
             ,L:(type)=>[[ 0, -1, 2], [ 0,  1, 3], [ 1,  0, 1], [-1,  0, 0]][type]
             ,R:(type)=>[[ 0,  1, 3], [ 0, -1, 2], [-1,  0, 0], [ 1,  0, 1]][type]};

class Node {
    constructor(s) {
        this.s = s;
        this.move = Array(4).fill(false);
        this.next = MOVE[s];
    }
}

function solution(grid) {
    grid = grid.map(a=>a.split("").map(b=>new Node(b)));
    var answer = [];
    for(let i = 0; i < grid.length; i++) {
        for(let j = 0; j < grid[i].length; j++) {
            for(let k = 0; k < 4; k++) {
                let count = 0;
                let [r, c, t] = [i, j, k];
                while(!grid[r][c].move[t]) {
                    grid[r][c].move[t] = true;
                    let [tr, tc, tt] = grid[r][c].next(t);
                    r = (grid.length + r + tr) % grid.length;
                    c = (grid[i].length + c + tc) % grid[i].length;
                    t = tt;
                    count++;
                }
                answer.push(count);
            }
        }
    }
    return answer.filter((_)=>_>0).sort((a,b)=>a-b);
}