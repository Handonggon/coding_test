function solution(wallpaper) {
    let [y1, x1, y2, x2] = [wallpaper.length, wallpaper[wallpaper.length -1].length, 0, 0];
    for(let i = 0; i < wallpaper.length; i++) {
        for(let j = 0; j < wallpaper[i].length; j++) {
            if(wallpaper[i][j] === '.') continue;
            y1 = Math.min(y1, i);
            x1 = Math.min(x1, j);
            y2 = Math.max(y2, i + 1);
            x2 = Math.max(x2, j + 1);
        }
    }
    return [y1, x1, y2, x2];
}