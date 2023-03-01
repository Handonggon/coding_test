function solution(a, b, n) {
    let answer = 0;
    while(n >= a) {
        let count = (parseInt(n / a) * b);
        answer += count;
        n = count + (n % a);
    }
    return answer;
}