/*
const set = [1, 1, 0, 1, 1];
function solution(n, l, r) {
    let answer = 0;
    let getValue = (loc)=>{
        if(loc < 5) return set[loc];
        if(loc % 5 === 2) return 0;
        return getValue(Math.floor(loc / 5));
    }
    for(let i = l - 1; i < r; i++) {
        answer += getValue(i);
    }
    return answer;
}
*/
function solution(n, l, r) {
    let answer = 0;
    for(let i = l - 1; i < r; i++) {
        console.log(i, i.toString(5))
        if (!i.toString(5).match('2')) answer += 1;
    }
    return answer;
}