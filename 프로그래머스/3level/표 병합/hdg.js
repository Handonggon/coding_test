const parent = {};

function find([r, c]) {
    if(parent[`${r}-${c}`]) return find(parent[`${r}-${c}`]);
    return parent[`${r}-${c}`] ? parent[`${r}-${c}`] : [r, c];
}

function solution(commands) {
    commands = commands.reverse().map(c=>c.split(" "));
    let table = Array.from(Array(51), ()=>Array(51).fill("EMPTY"));
    
    let answer = [];
    while(commands.length) {
        let [type, ...input] = commands.pop();
        switch(type) {
            case "UPDATE": {
                if(input.length == 3) {
                    let [r, c, value] = input;
                    [r, c] = find([r, c]);
                    for(let i = 0; i < table.length; i++) {
                        for(let j = 0; j < table[i].length; j++) {
                            let [tr, tc] = find([i, j]);
                            if(r == tr && c == tc) table[i][j] = value;
                        }
                    }
                } else {
                    let [value1, value2] = input;
                    for(let i = 0; i < table.length; i++) {
                        for(let j = 0; j < table[i].length; j++) {
                            if(table[i][j] == value1) table[i][j] = value2;
                        }
                    }
                }
                break;
            }
            case "MERGE": {
                let [r1, c1, r2, c2] = input;
                let value = "";
                if(table[r1][c1] == "EMPTY") value = table[r2][c2];
                else value = table[r1][c1];
                
                [r1, c1] = find([r1, c1]);
                [r2, c2] = find([r2, c2]);
                if(r1 == r2 && c1 == c2) break;
                parent[`${r2}-${c2}`] = [r1, c1];
                commands.push(["UPDATE", r1, c1, value]);
                break;
            }
            case "UNMERGE": {
                let [r, c] = input;
                commands.push(["UPDATE", r, c, table[r][c]]);
                [r, c] = find(input);
                
                let memory = [];
                for(let i = 0; i < table.length; i++) {
                    for(let j = 0; j < table[i].length; j++) {
                        let [tr, tc] = find([i, j]);
                        if(r == tr && c == tc) memory.push([i, j]);
                    }
                }
                for(let [i, j] of memory) {
                    table[i][j] = "EMPTY";
                    parent[`${i}-${j}`] = undefined;
                }
                break;
            }
            case "PRINT": {
                let [r, c] = input;
                answer.push(table[r][c])
                break;
            }
        }
    }
    return answer;
}