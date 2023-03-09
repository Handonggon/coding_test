Array.prototype.set = function(index, valure) {
    this[Number(index)] = valure;
    return this;
}
const counting = (list)=>list.reduce((acc, cur)=>acc.set(cur, acc[cur] + 1), Array(10).fill(0));

function solution(X, Y) {
    let numberX = counting(X.split(""));
    let numberY = counting(Y.split(""));
    let answer = [...Array(10).keys()].map((index)=>String(index).repeat(Math.min(numberX[index], numberY[index])))
                              .reverse().join("");
    if(answer === "") return "-1";
    else if(answer[0] === "0") return "0";
    return answer;
}