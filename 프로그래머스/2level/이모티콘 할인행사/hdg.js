const DISCOUNT = [10, 20, 30, 40];

function solution(users, emoticons) {
    function dfs(list) {
        if(list.length === emoticons.length) {
            let [sub, amount] = [0, 0];
            for(let [minRate, maxPrice] of users) {
                let sum = 0;
                for(let [rate, emoticon] of list) {
                    if(rate >= minRate) {
                        sum += (emoticon - (emoticon * (rate / 100)));
                    }
                }
                if(sum >= maxPrice) sub += 1;
                else amount += sum;
            }
            return [sub, amount];
        }
        let answer = [];
        for(let rate of DISCOUNT) {
            answer.push(dfs([...list, [rate, emoticons[list.length]]]));
        }
        return answer.sort(([sub1, amount1], [sub2, amount2])=>{
            if(sub1 === sub2) {
                return amount2 - amount1;
            }
            return sub2 - sub1;
        })[0];
    }
    return dfs([]);
}