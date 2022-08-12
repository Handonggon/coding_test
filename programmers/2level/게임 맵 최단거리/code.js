function solution(maps) {
    return BFS(maps);
}

var dy = [0, -1, 0, 1];
var dx = [-1, 0, 1, 0]

function BFS(maps) {
    var queue = new Array();
    queue.push({"y":0, "x":0});
    while(queue.length > 0) {
        var loc = queue.shift();
        for(var i = 0; i < 4; i++) { //4방향
            var ny = loc["y"] + dy[i];
            var nx = loc["x"] + dx[i];
            
            if(ny >= 0 && ny < maps.length && nx >= 0 && nx < maps[0].length && maps[ny][nx] == 1) {
                maps[ny][nx] = maps[loc["y"]][loc["x"]] + 1;
                queue.push({"y":ny, "x":nx});
            }   
        }
    }
    if(maps[maps.length-1][maps[0].length-1] == 1) return -1;
    return maps[maps.length-1][maps[0].length-1];
}