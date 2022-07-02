function solution(board, moves) {
    var answer = 0;
    
    var baguni = [];
    for(var i = 0; i < moves.length; i++) {
        for(var j = 0; j < board[0].length; j++) {
            if(board[j][moves[i]-1] > 0) {
                baguni.push(board[j][moves[i]-1]);
                board[j][moves[i]-1] = 0;
                break;
            }
        }
    }
    var count = 0;
    var result = [];
    for(var i = 0; i < baguni.length; i++) {
        var item = baguni[i];
        if(result.length>0) {
            var pItem = result.pop();
            if(item == pItem) {
                count += 2;
            } else {
                result.push(pItem);
                result.push(item);
            }
        } else {
            result.push(item);
        }
    }
    return count;
}
