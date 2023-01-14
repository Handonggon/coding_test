function solution(t, p) {
    let answer = 0;
    for(let i = 0; i + p.length <= t.length; i++) {
        if(Number(p) >= Number(t.substr(i, p.length))) {
            answer += 1;
        }
    }
    return answer;
}