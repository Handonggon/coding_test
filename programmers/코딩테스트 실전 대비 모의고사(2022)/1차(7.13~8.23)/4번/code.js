function solution(beginning, target) {
    let N = beginning.length;

    for(let i = 0; i < Math.pow(2, N); i++) {
        for(let j = 0; j < Math.pow(2, N); j++) {
            let mask = Array(N).fill(0).map(()=>Array(N).fill(false));
            for(let r = 0; r < N; r++) {
                if(r & i) mask[r] = mask[r].map(_=>!_);
            }
            for(let c = 0; c < N; c++) {
                if(c & j) {
                    for(let r = 0; r < N; r++) {
                        mask[r][c] = !mask[r][c];
                    }
                }
            }
        }
    }
    var answer = 0;
    return answer;
}
