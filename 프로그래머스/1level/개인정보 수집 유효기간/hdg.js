function solution(today, terms, privacies) {
    today = new Date(today);
    let typeToMm = {};
    for(let [type, mm] of terms.map(term=>term.split(" "))) {
        typeToMm[type] = Number(mm);
    }
    
    var answer = [];
    for(let [index, prev, type] of privacies.map((privacie, index)=>[index + 1, ...privacie.split(" ")])) {
        prev = new Date(prev);
        if(new Date(prev.setMonth(prev.getMonth() + typeToMm[type])) <= today) {
            answer.push(index);
        }
    }
    return answer;
}