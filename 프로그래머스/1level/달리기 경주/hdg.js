function solution(players, callings) {
    let playerOrder = players.reduce((obj, player, order)=>{
        obj[player] = order;
        return obj;
    }, {});
    for(let calling of callings) {
        let origin = playerOrder[calling];
        let target = origin - 1;
        [playerOrder[calling], playerOrder[players[target]]] = [target, origin];
        [players[target], players[origin]] = [players[origin], players[target]];
    }
    return players;
}