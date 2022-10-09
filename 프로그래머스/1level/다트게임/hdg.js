const BONUS = {"S":1, "D":2, "T":3}

function solution(dartResult) { 
    var answer = 0;
    
    var score = new Array(); 
    var bonus = new Array(); 
    var option = new Array(); 
    for(var i = 0; i < dartResult.length; i++) {
        var ch = String(dartResult[i]);
        
        if(ch == "S" || ch == "D" || ch == "T") {
            bonus.push(ch);
        } else if(ch == "*" || ch == "#") {
            option[bonus.length-1] = ch;
        } else {
            if(dartResult[i+1] == "0") {
                score.push(10);
                i++;
            } else {
                score.push(ch);
            }
            
        }
    }
    
    for(var i = score.length-1; i >= 0; i--) {
        var resuult = Math.pow(score[i], BONUS[bonus[i]]);
        if(option[i] != "undefined") {
            if(option[i] == "*") {
                resuult *= 2;
            } else if(option[i] == "#") {
                resuult *= -1;
            }   
        }
        if(option[i+1] != "undefined" && option[i+1] == "*") {
            resuult *= 2;
        }
        answer += resuult;
    }
    return answer;
}