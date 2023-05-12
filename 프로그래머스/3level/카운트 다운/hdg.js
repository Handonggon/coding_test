const compare = ([c1, sp1], [c2, sp2])=>{
    if(c1 === c2) return (sp1 > sp2) ? [c1, sp1] : [c2, sp2];
    return (c1 > c2) ? [c2, sp2] : [c1, sp1];
}

function solution(target) {
    let answer = Array.from(Array(target + 1), ()=>false);
    for(let score = 1; score <= 20; score++) {
        answer[score] = [1, 1];
        answer[score * 2] = [1, 0];
        answer[score * 3] = [1, 0];
    }
    answer[50] = [1, 1];

    for(let i = 1; i < answer.length; i++) {
        if(answer[i]) continue;
        answer[i] = [i, 0];
        for(let score = 1; score <= 20; score++) {
            if(i >= score) {
                let [c, sp] = answer[i - score];
                answer[i] = compare(answer[i], [c + 1, sp + 1]);
            }
            if(i >= score * 2) {
                let [c, sp] = answer[i - (score * 2)];
                answer[i] = compare(answer[i], [c + 1, sp]);
            }
            if(i >= score * 3) {
                let [c, sp] = answer[i - (score * 3)];
                answer[i] = compare(answer[i], [c + 1, sp]);
            }
        }
        if(i >= 50) {
            let [c, sp] = answer[i - 50];
            answer[i] = compare(answer[i], [c + 1, sp + 1]);
        }
    }
    return answer[target];
}