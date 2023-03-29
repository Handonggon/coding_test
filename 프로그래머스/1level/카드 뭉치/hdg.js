function solution(cards1, cards2, goal) {
    cards1 = cards1.reverse();
    cards2 = cards2.reverse();
    return goal.reduce((answer, str)=>{
        if(cards1[cards1.length - 1] === str) {
            cards1.pop();
            return answer;
        }
        if(cards2[cards2.length - 1] === str) {
            cards2.pop();
            return answer;
        }
        return "No";
    }, "Yes");
}