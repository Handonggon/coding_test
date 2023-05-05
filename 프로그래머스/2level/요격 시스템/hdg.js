const INF = 100000001;

function solution(targets) {
    targets = [...targets.sort(([s1, e1], [s2, e2])=>s1 - s2), [INF, 0]];

    let answer = 0;
    let min = INF;
    for(let [s, e] of targets) {
        if(s >= min) {
            answer += 1;
            min = INF;
        }
        min = Math.min(e, min);
    }
    return answer;
}