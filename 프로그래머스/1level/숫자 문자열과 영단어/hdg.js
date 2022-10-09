const transList = {zero:"0", one:"1", two:"2", three:"3", four:"4", five:"5", six:"6", seven:"7", eight:"8", nine:"9"};

function solution(s) {
    var answer = new Array();
    
    let word = "";
    for(let char of s) {
        if(char >= "0" && char <= "9") {
            answer.push(char);
        } else {
            word += char;
            if(transList[word]) {
                answer.push(transList[word]);
                word = "";
            }
        }
    }
    return Number(answer.join(""));
}