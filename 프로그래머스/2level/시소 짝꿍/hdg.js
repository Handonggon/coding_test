const SCALE = [2/3, 2/4, 3/4];

function solution(weights) {
    let answer = {};
    for(let weight of weights) {
        if(weight in answer) answer[weight]++;
        else answer[weight] = 1;
    }
    return Object.keys(answer).map(weight=>{
        let count = Array.from(Array(answer[weight]), (_, n)=>n).reduce((a, b)=>a + b);
        for(let scale of SCALE) {
            if((weight * scale) in answer) count += (answer[weight * scale] * answer[weight]);
        }
        return count;
    }).reduce((a, b)=>a + b);
}