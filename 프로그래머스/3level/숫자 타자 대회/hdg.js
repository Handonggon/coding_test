const INF = 1000000;
const LOCATION = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['*', '0', '#']];

function getPoint(number) {
    for(let y = 0; y < LOCATION.length; y++) {
        for(let x = 0; x < LOCATION[y].length; x++) {
            if(LOCATION[y][x] === String(number)) return [y, x];
        }
    }
}

function solution(numbers) {
    const DISTANCE = Array.from(Array(10), ()=>Array(10).fill(0));
    for(let i = 0; i < DISTANCE.length; i++) {
        for(let j = 0; j < DISTANCE[i].length; j++) {
            if(i === j) {
                DISTANCE[i][j] = 1;
            } else {
                let [y1, x1] = getPoint(i);
                let [y2, x2] = getPoint(j);
                let [dy, dx] = [Math.abs(y1 - y2), Math.abs(x1 - x2)];
                let max = Math.max(dy, dx);
                let min = Math.min(dy, dx);
                DISTANCE[i][j] = (Math.min(dy, dx) * 3) + ((max - min) * 2);
            }
        }
    }

    let dp = Array.from(Array(numbers.length + 1), ()=>Array.from(Array(10), ()=>Array(10).fill(INF)));
    dp[0][4][6] = 0;

    for(let seq = 0; seq < numbers.length; seq++) {
        let curr = parseInt(numbers[seq]);

        for(let i = 0; i < DISTANCE.length; i++) {
            for(let j = 0; j < DISTANCE[i].length; j++) {
                if(i === j) continue;

                dp[seq + 1][curr][j] = Math.min(dp[seq + 1][curr][j], dp[seq][i][j] + DISTANCE[i][curr]);
                dp[seq + 1][i][curr] = Math.min(dp[seq + 1][i][curr], dp[seq][i][j] + DISTANCE[j][curr]);
            }
        }
    }
    return Math.min(...dp[numbers.length].flat())
}