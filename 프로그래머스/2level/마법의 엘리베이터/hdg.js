function solution(storey) {
    let answer = 0
    while(storey) {
        let rem = storey % 10
        storey = parseInt(storey / 10)
        if(rem > 5) {
            storey += 1;
            answer += (10 - rem);
        } else if(rem === 5 && storey % 10 >= 5) {
            storey += 1;
            answer += 5;
        } else {
            answer += rem;
        }
    }
    return answer;
}