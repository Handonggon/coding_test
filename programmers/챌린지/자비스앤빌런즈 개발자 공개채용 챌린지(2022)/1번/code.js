function solution(students) {
    let info = [];
    for(let index = 0; index < students.length; index++) {
        let A = students[index].match(/A/g)?.length | 0;
        let L = students[index].match(/L/g)?.length | 0;
        let P = students[index].match(/P/g)?.length | 0;
        P = P + Math.floor(L / 2);
        let score = 10 + A - P
        if(P >= 3) score = 0;

        info.push([score, students.length - index]);
    }

    var answer = [];
    return info.sort((a,b)=>{
        for(let i = 0; i < 3; i++) {
            if(a[i] === b[i]) continue;
            return b[i] - a[i];
        }
    }).map(x=>students.length - x[1] + 1);
}