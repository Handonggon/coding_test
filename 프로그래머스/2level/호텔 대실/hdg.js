let getTime = (hm)=>{
    let [h, m] = hm.split(":");
    return (60 * h) + +m;
}

function solution(book_time) {
    let dp = Array(24 * 60).fill(0);
    for(let [hm, i] of book_time.flat().map((hm, i)=>[hm, i])) {
        dp[Math.min(getTime(hm) + ((i % 2) * 10), dp.length - 1)] += Math.pow(-1, i);
    }
    for(let i = 1; i < dp.length; i++) {
        dp[i] = dp[i] + dp[i - 1];
    }
    return Math.max(...dp);
}