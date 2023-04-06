function solution(sequence) {
    let answer = 0;
    let dpFwd = [];
    let dpRvs = [];
    for(let i = 0; i < sequence.length; i++) {
        let [forward, reverse] = [(Math.pow(-1, i) * sequence[i]), (Math.pow(-1, i + 1) * sequence[i])];
        if(i === 0) {
            dpFwd.push(forward);
            dpRvs.push(reverse);
        } else {
            dpFwd.push(Math.max(forward, dpFwd[i - 1] + forward));
            dpRvs.push(Math.max(reverse, dpRvs[i - 1] + reverse));
        }
        answer = Math.max(answer, dpFwd[i], dpRvs[i]);
    }
    return answer;
}

/*
function solution(sequence) {
    let m = 0, M = 0;
    let acc = m;

    for (let i = 0; i < sequence.length; i++) {
        acc = ((i % 2 == 1) ? (acc - sequence[i]) : (acc + sequence[i]));
        M = Math.max(M, acc);
        m = Math.min(m, acc);
    }
    return M == m ? M : M - m;
}
*/