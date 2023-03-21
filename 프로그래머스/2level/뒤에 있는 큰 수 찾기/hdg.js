Array.prototype.peek = function() { return this.length > 0 ? this[this.length - 1] : undefined; };

function solution(numbers) {
    let dp = {};
    let stack = [];
    for(let index = 0; index < numbers.length; index++) {
        let number = numbers[index];
        while(stack.length) {
            if(numbers[index] <= numbers[stack.peek()]) break;
            dp[stack.pop()] = index;
        }
        stack.push(index);
    }
    while(stack.length) {
        dp[stack.pop()] = -1;
    }
    return numbers.map((_, index)=>dp[index] > -1 ? numbers[dp[index]] : -1);
}