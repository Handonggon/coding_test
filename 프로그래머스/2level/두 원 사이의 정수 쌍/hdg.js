function solution(r1, r2) {
    let answer = 0;
    for(let x = 1; x <= r2; x++) {
        let max = Math.floor(Math.sqrt(Math.pow(r2, 2) - Math.pow(x, 2)));
        let min = x > r1 ? 0 : Math.ceil(Math.sqrt(Math.pow(r1, 2) - Math.pow(x, 2)))
        answer = answer + max - min + 1;
    }
    return 4 * answer;
}