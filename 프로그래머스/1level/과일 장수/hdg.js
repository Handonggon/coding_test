function solution(k, m, score) {
    var answer = Array(k).fill(0);
    for(let s of score) {
        answer[k - s] += 1
    }
    return answer.reduce(([benefit, remain], count, index)=>{
        return [benefit + ((k - index) * parseInt((count + remain) / m) * m), (count + remain) % m]
    }, [0, 0])[0];
}