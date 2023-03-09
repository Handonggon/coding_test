let [O, X] = [0, 1];
function solution(s) {
    let answer = 0;
    let x = "";
    let count = [0, 0];
    for(let c of s) {
        if(count[O] === 0) x = c;

        if(x === c) count[O]++;
        else count[X]++;

        if(count[O] === count[X]) {
            answer++;
            count = [0, 0];
        }
    }
    return answer + (count[O] > 0 ? 1 : 0);
}