function solution(cards) {
    let answer = [];
    let vsited = Array(cards.length).fill(false);
    for(let card of cards.map(card=>card - 1)) {
        let count = 0;
        while(!vsited[card]) {
            vsited[card] = true;
            card = cards[card] - 1;
            count++;
        }
        answer.push(count);
    }
    let [first, second, ...other] = answer.sort((a, b)=>b - a);
    return first * second;
}