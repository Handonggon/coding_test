function solution(want, number, discount) {
    let basket = {};
    for(let i = 0; i < want.length; i++) {
        basket[want[i]] = number[i];
    }
    let answer = 0;
    for(let i = 0; i+10 <= discount.length; i++) {
        let temp = {};
        for(let j = i; j < i+10; j++) {
           if(!temp[discount[j]]) temp[discount[j]] = 0;
           temp[discount[j]] += 1;
        }
        let check = true;
        for(let key in basket) {
            if(basket[key] <= temp[key]) continue;
            check = false;
            break;
        }
        if(check) answer += 1;
    }
    return answer;
}