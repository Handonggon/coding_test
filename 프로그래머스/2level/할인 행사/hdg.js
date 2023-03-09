function solution(want, number, discount) {
    let answer = 0;
    for(let i = 0; i < discount.length; i++) {
        let map = new Map(want.map((_, i)=>[want[i], number[i]]));
        for(let j = i; j < Math.min(i + 10, discount.length); j++) {
            if(map.has(discount[j])) {
                let count = map.get(discount[j]) - 1;
                if(count === 0) map.delete(discount[j]);
                else map.set(discount[j], count);
            }
        }
        answer += (map.size == 0 ? 1 : 0);
    }
    return answer;
}