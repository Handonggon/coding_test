function isPossible(binary) {
    let stack = [[0, binary.length - 1, "1"]];
    while(stack.length) {
        let [left, right, isEnd] = stack.pop();
        if(left > right) continue;
        let mid = Math.floor((left + right) / 2);
        if(isEnd === "0" && binary[mid] === "1") return 0;

        stack.push([left, mid - 1, binary[mid]]);
        stack.push([mid + 1, right, binary[mid]]);
    }
    return 1;
}

function solution(numbers) {
    var answer = [];
    for(let number of numbers) {
        let binary = number.toString(2);
        let level = 1;
        while(binary.length > Math.pow(2, level) - 1) level++;
        answer.push(isPossible("0".repeat(Math.pow(2, level) - 1 - binary.length) + binary));
    }
    return answer;
}