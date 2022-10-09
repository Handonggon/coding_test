function solution(distance, scope, times) {
    let info = {};
    for(let i = 0; i < scope.length; i++) {
        let [a, b] = scope[i];
        for(let key = Math.min(a, b); key <= Math.max(a, b); key++) {
            info[key] = times[i];
        }
    }

    let answer = 0;
    do {
        answer += 1;
        if(info[answer]) {
            let [work, rest] = info[answer];
            if(work > (answer-1) % (work+rest)) {
                break;
            }
        }
    } while(answer < distance);
    return answer;
}