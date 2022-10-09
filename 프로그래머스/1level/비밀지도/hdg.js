function solution(n, arr1, arr2) {
    var answer = new Array(n);
    for(var i = 0; i < n; i++) {
        
        var rowNum = arr1[i] | arr2[i];
        answer[i] = '0'.repeat(n) + rowNum.toString(2);
        answer[i] = answer[i].slice(answer[i].length-n, answer[i].length);
        
    }
    return answer.map((x)=>String(x).replace(/1/gi, "#").replace(/0/gi, " "));
}