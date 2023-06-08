function solution(n, results) {
    let tree = Array(n).fill().map(_=>[]);
    for(let [win, lose] of results) {
        tree[win-1].push(lose-1);
    }
    
    
    let win = Array(n).fill().map(_=>Array(n).fill(""));
    for(let player = 0; player < n; player++) {
        let visit = Array(n).fill().map((_,i)=>i===player);
        
        let stack = new Array();
        stack.push(player);
        while(stack.length) {
            let prov = stack.pop();
            for(let next of tree[prov]) {
                if(visit[next]) continue;
                stack.push(next);
                visit[next] = true;
                win[player][next] = true;
                win[next][player] = false;
            }
        } 
    }
    return win.filter(x=>x.filter(y=>y!=="").length===n-1).length;
}