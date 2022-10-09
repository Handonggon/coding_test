function solution(numbers, hand) {
    var answer = '';
    var left = 10;
    var rigth = 12;
    
    for(var i in numbers) {
        if('[147]'.match(numbers[i])) {
            answer += 'L';
        } else if('[369]'.match(numbers[i])) {
            answer += 'R';
        } else {
            if(numbers[i] == 0) numbers[i] = 11;

            var distL = dist(Math.abs(numbers[i]-left));
            var distR = dist(Math.abs(numbers[i]-rigth));
            
            if(distL == distR) {
                if(hand == "left") {
                    answer += 'L';
                } else if(hand == "right") {
                    answer += 'R';
                }
            } else if(distL > distR) {
                answer += 'R';
            } else {
                answer += 'L';
            }
        }
        if(answer[i] == 'L') {
            left = numbers[i];
        } else if(answer[i] == 'R') {
            rigth = numbers[i];
        }            
    }
    return answer;
}

function dist(sub) {
    if(sub == 0) {
        return 0;
    } else if(sub == 1 || sub == 3) {
        return 1;
    } else if(sub == 2 || sub == 4 || sub == 6) {
        return 2;
    } else if(sub == 5 || sub == 7 || sub == 9) {
        return 3;
    } else {
        return 4;
    }
}
