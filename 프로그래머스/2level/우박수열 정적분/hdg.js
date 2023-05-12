function solution(k, ranges) {
    let set = [k];
    while(k > 1) {
        if(k % 2 === 0) k = k / 2;
        else k = 3 * k + 1;
        set.push(k);
    }
    return ranges.map(([s, e])=>[s, set.length + e - 1]).map(([s, e])=>{
        if(s > e) return -1;
        if(s === e) return 0;
        
        let answer = 0;
        for(let i = s; i < e; i++) {
            let max = Math.max(set[i], set[i + 1]);
            let min = Math.min(set[i], set[i + 1]);
            answer += min + ((max - min) / 2);
        }
        return answer;
    });
}