const [N, E, S, W] = [0, 1, 2, 3];
const DIR = [[0, 0], [0, -1], [-1, 0], [0, 1], [1, 0]];

function solution(clockHands) {
    const isBoundary = (y, x)=>(y >= 0 && y < clockHands.length && x >= 0 && x < clockHands[y].length);
    const rotation = (clockHands, y, x, r)=>{
        DIR.filter(([dy, dx])=>isBoundary(dy + y, dx + x)).forEach(([dy, dx])=>{
            clockHands[dy + y][dx + x] = ((4 + clockHands[dy + y][dx + x] + r) % 4);
        });
    }
    const countingRemain = (clockHands)=>{
        let count = 0;
        for(let y = 1; y < clockHands.length; y++) {
            for(let x = 0; x < clockHands[y].length; x++) {
                for(let r = 0; r < 4; r++) {
                    if(((clockHands[y - 1][x] + r) % 4) === N) {
                        count += r;
                        rotation(clockHands, y, x, r);
                        break;
                    }
                }
            }
        }
        return clockHands.every(row=>row.every(cell=>cell === N)) ? count : Number.MAX_VALUE;
    }
    
    function dfs(x) {
        if(x >= clockHands[0].length) return countingRemain(clockHands.map(row=>[...row]));
        let count = Number.MAX_VALUE;
        for(let r = 0; r < 4; r++) {
            rotation(clockHands, 0, x, r);
            count = Math.min(count, dfs(x + 1) + r);
            rotation(clockHands, 0, x, -r);
        }
        return count;
    }
    return dfs(0);
}