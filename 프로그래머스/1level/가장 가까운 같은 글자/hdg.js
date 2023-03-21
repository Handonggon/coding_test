function solution(s) {
    var answer = [];
    let dp = {};
    for(let i = 0; i < s.length; i++) {
        if(dp.hasOwnProperty(s[i])) {
            answer.push(i - dp[s[i]]);
        } else {
            answer.push(-1);
        }
        dp[s[i]] = i;
    }
    return answer;
}