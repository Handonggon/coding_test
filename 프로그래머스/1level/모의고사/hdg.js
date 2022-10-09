function solution(answers) {
    var answer = [];
    
    var student = [];
    student[0] = [1,2,3,4,5];
    student[1] = [2,1,2,3,2,4,2,5];
    student[2] = [3,3,1,1,2,2,4,4,5,5];
    
    for(var i in answers) {
        for(var j = 0; j < student.length; j++) {
            if(!answer[j]) answer[j] = 0;
            if(answers[i] === student[j][(i%student[j].length)]) {
                answer[j]++;
            }
        }
    }
    
    var result = [];
    var max = Math.max(...answer);
    for(var i in answer) {
        if(max == answer[i]) {
            result.push(Number(i)+1);
        }
    }
    
    return result.sort((x,y)=>x-y);
}