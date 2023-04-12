const [NAME, PLAY, START] = [0, 1, 2];
let hhmmToMinute = (hhmm)=>{
    let [hh, mm] = hhmm.split(":").map(n=>+n);
    return (hh * 60) + mm;
}

function solution(plans) {
    let answer = [];
    plans = [...plans.map(([name, start, playtime])=>[name, playtime, hhmmToMinute(start)])
                 .sort((a, b)=>a[START] - b[START]), ["", 0, 101440]];
    let stack = [];
    for(let i = 1; i < plans.length; i++) {
        let interval = plans[i][START] - plans[i - 1][START];
        stack.push([plans[i - 1][NAME], plans[i - 1][PLAY]]);
        while(interval > 0 && stack.length) {
            let curr = stack.pop();
            if(curr[PLAY] > interval) {
                stack.push([curr[NAME], curr[PLAY] - interval]);
            } else {
                answer.push(curr[NAME]);
            }
            interval -= curr[PLAY];
        }
    }
    return answer;
}