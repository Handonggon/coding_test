function solution(scores) {
    let [ta, tb] = scores[0];
    
    let max = 0;
    let summary = [];
    for(let [a, b] of scores.sort(([a1, b1], [a2, b2])=>(a1 === a2) ? b1 - b2 : a2 - a1)) {
        if(max > b) {
            if(a === ta && b === tb) return -1;
        } else {
            summary.push(a + b);
            max = Math.max(max, b);
        }
    }
    return summary.sort((a, b)=>b - a).indexOf(ta + tb) + 1;
}