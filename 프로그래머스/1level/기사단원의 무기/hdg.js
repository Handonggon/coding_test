function solution(number, limit, power) {
    let answer = Array(number + 1).fill(0);
    for(let i = 1; i <= number; i++) {
        for(let j = 1; i * j <= number; j++) {
            answer[i * j]++;
        }
    }
    return answer.map(p=>(p > limit ? power : p)).reduce((acc, cur)=>acc + cur);
}