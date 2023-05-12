function solution(cap, n, deliveries, pickups) {
    let answer = 0;
    let [d, p] = [0, 0];
    
    for(let i = n; i > 0; i--) {
        d += deliveries[i - 1];
        p += pickups[i - 1];
        while(d > 0 || p > 0) {
            d -= cap;
            p -= cap;
            answer += (2 * i);
        }
    }
    return answer;
}