/*
function solution(e, starts) {
    starts = starts.map((start, i)=>[start, i]).sort(([s1, i1], [s2, i2])=>s1-s2);
    let dp = Array(e + 1).fill(1);
    for(let n = 2; n <= e; n++) {
        let multiple = n;
        while(multiple <= e) {
            dp[multiple] += 1;
            multiple += n;
        }
    }
    let answer = Array(starts.length).fill(0);
    let [max, index] = [0, e];
    for(let i = e; i >= 0; i--) {
        if(dp[i] >= max) {
            max = dp[i];
            index = i;
        }
        if(starts[starts.length - 1][0] === i) {
            answer[starts[starts.length - 1][1]] = index;
            starts.pop();
        }
        if(starts.length === 0) break;
    }
    return answer;
}
*/

function solution(e, starts) {
    let numCnt = Array(e + 1).fill(1);
    for (let i = 2; i <= e; i++) {
        for (let j = 1; j <= e / i; j++) numCnt[i * j]++;
    }
    let dp = Array(e + 1).fill(0);
    let [max, maxIdx] = [0, 0];
    let start = Math.min(...starts);
    for(let n = e; n >= start; n--) {
        if(numCnt[n] >= max) {
            max = numCnt[n];
            maxIdx = n;
        }
        dp[n] = maxIdx;
    }
    return starts.map(start=>dp[start]);
}
