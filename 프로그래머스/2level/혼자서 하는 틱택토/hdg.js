function solution(board) {
    let count = {"O": 0, "X": 0, ".": 0};
    for(let mark of board.flat().join("")) {
        count[mark] += 1;
    }
    let gap = count["O"] - count["X"];
    if(0 <= gap && gap <= 1) {
        let plan = [...board
                  , ...board.map((_, i)=>board.map(r=>r[i]).join(""))
                  , board[0][0] + board[1][1] + board[2][2]
                  , board[0][2] + board[1][1] + board[2][0]];
        
        let [winO, winX] = plan.reduce(([winO, winX], curr)=>{
            if(curr === "OOO") winO += 1;
            if(curr === "XXX") winX += 1;
            return [winO, winX];
        }, [0, 0]);
        
        if(winO > 0 && winX > 0) return 0;
        if(winO > 0 && count["O"] === count["X"]) return 0;
        if(winX > 0 && count["O"] !== count["X"]) return 0;
        return 1;
    }
    return 0;
}