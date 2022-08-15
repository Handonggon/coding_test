function solution(n, lighthouse) {
    let map = Array(n).fill().map(_=>[]);
    for(let [v, w] of lighthouse) {
        map[v-1].push(w-1);
        map[w-1].push(v-1);
    }

    let seq = Array(n).fill().map((_, index)=>index).sort((a, b)=>{
        return map[a].length - map[b].length;
    });

    let answer = 0;
    let light = n;
    while(light>0) {
        let curr = seq.pop();
        for(let next of [...map[curr], curr]) {
            if(light[next]) continue;
            light[next] = true;
            light -= 1;
        }
        answer += 1;
    }
    return answer;
}

/*
function solution(n, lighthouse) {
    let map = Array(n).fill().map(_=>Array(n).fill(false));
    for(let [v, w] of lighthouse) {
        map[v-1][w-1] = true;
        map[w-1][v-1] = true;
    }

    let answer = 0;
    


}
*/