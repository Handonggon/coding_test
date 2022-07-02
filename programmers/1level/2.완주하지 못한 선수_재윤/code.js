function solution(participant, completion) {
    var map = {};
    
    for(var i in participant) {
        if(!map[participant[i]]) { map[participant[i]] = 1; }
        else { map[participant[i]]++; }
    }
    
    for(var i in completion) {
        if(!map[completion[i]]) { map[completion[i]] = 1; }
        else { map[completion[i]]++; }
    }       
    
    var answer = "";
    for(var key in map) {
        if(map[key]%2 == 1) {
            answer = key;
            break;
        }
    }
    return answer;
}
