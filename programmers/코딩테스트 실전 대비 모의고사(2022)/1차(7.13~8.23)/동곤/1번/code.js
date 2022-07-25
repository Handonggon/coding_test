function solution(X, Y) {
    let [x, y] = [Array(10).fill(0), Array(10).fill(0)];

    for(let _x of X.split("")) {
        x[Number(_x)] += 1;
    }
    for(let _y of Y.split("")) {
        y[Number(_y)] += 1;
    }
    let answer = "";
    for(let number = 9; number >= 0; number--) {
        let count = Math.min(x[number], y[number]);
        if(number === 0 && answer.length === 0 && count > 0) return "0";
        for(let c = 0; c < count; c++) answer += number;
    }
    return answer.length ? answer : "-1";
}