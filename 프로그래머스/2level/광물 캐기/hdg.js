const INTERVAL = 5;
const INF = 750;
function solution(picks, minerals) {
    let table = [{"diamond": 1, "iron": 1, "stone": 1}
                , {"diamond": 5, "iron": 1, "stone": 1}
                , {"diamond": 25, "iron": 5, "stone": 1}];
    
    function dfs(picks, point) {
        let [start, end] = [point * INTERVAL, (point + 1) * INTERVAL];
        if(start >= minerals.length || picks.every(pick=>pick===0)) return 0;
        
        let pirodo = INF;
        for(let index = 0; index < picks.length; index++) {
            if(picks[index] === 0) continue;
            picks[index]--;
            let curr = minerals.slice(start, end).map(mineral=>table[index][mineral]).reduce((a, b)=>a + b);
            let next = dfs(picks, point + 1);
            pirodo = Math.min(pirodo, curr + next);
            picks[index]++;
        }
        return pirodo;
    }
    return dfs(picks, 0);
}