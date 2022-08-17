function solution(beginning, target) {
    let N = beginning.length;
    let M = beginning[0].length;

    let answer = N + M + 1;
    for(let i = 0; i < Math.pow(2, N); i++) {
        for(let j = 0; j < Math.pow(2, M); j++) {
            let check = true;
            for(let r = 0; r < beginning.length; r++) {
                for(let c = 0; c < beginning[r].length; c++) {
                    if(((Boolean(1 << r & i) ^ Boolean(1 << c & j)) ^ beginning[r][c]) === target[r][c]) continue;
                    check = false;
                    break;
                }
                if(!check) break;
            }
            if(check) {
                answer = Math.min(answer, i.toString(2).split("").filter(_=>Number(_)).length + j.toString(2).split("").filter(_=>Number(_)).length);
            }
        }
    }
    return answer === N + M + 1 ? -1 : answer;
}
