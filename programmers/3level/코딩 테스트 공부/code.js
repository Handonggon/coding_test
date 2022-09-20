class Node {
    constructor(alp, cop, time) {
        this.alp = alp;
        this.cop = cop;
        this.time = time;
    }
}

function solution(alp, cop, problems) {
    problems.push([0, 0, 0, 1, 1]);
    problems.push([0, 0, 1, 0, 1]);
    
    let [alp_max, cop_max] = problems.reduce((tuple, problem)=>[Math.max(problem[0], tuple[0]), Math.max(problem[1], tuple[1])], [alp, cop]);
    
    let queue = [];
    queue.push(new Node(alp, cop, 0));
    
    let dp = Array(alp_max+1).fill().map(_=>Array(cop_max+1).fill(Number.MAX_VALUE));
    dp[alp][cop] = 0;
    while(queue.length) {
        let curr = queue.shift();
        for(let [alp_req, cop_req, alp_rwd, cop_rwd, cost] of problems) {
            if(curr.alp >= alp_req && curr.cop >= cop_req) {
                let next = new Node(Math.min(alp_max, curr.alp + alp_rwd), Math.min(cop_max, curr.cop + cop_rwd), curr.time + cost);
                if(dp[next.alp][next.cop] > next.time) {
                    for(let i = curr.alp; i <= next.alp; i++) {
                        for(let j = curr.cop; j <= next.cop; j++) {
                            dp[i][j] = Math.min(dp[i][j], next.time);
                        }
                    }
                    queue.push(next);
                }
            }
        }
    }
    return dp[alp_max][cop_max];
}