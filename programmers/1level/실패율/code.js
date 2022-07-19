function solution(N, stages) {
    var challenging = new Array(N+1); challenging.fill(0);
    var arrival = new Array(N+1); arrival.fill(0);
    for(var i in stages) {
        for(var j = 0; j < stages[i]-1; j++) {
            arrival[j]++;
        }
        challenging[stages[i]-1]++;
    }
    
    var failure = new Map();
    for(var i = 0; i < N; i++) {
        if(arrival[i]+challenging[i] == 0) {
            failure[i] = 0;
            continue; 
        }
        failure[i] = challenging[i] / (arrival[i]+challenging[i]);
    }
    
    var result = new Array();
    for(var key in failure) {
        var max = -1;
        var index = 0;
        for(var j = 0; j < N; j++) {
            if(!result.includes(j)) {
                if(failure[j] > max) {
                    index = j;
                    max = failure[j];
                }
            }
        }
        result.push(index);
    }
    return result.map((x)=>x+1);
}