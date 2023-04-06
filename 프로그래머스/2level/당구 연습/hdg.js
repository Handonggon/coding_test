function solution(m, n, startX, startY, balls) {
    return balls.map(([targetX, targetY])=>{
        let answer = [];
        if(!(startY === targetY && startX > targetX)) answer.push((targetX + startX)**2 + (targetY - startY)**2);
        if(!(startY === targetY && startX < targetX)) answer.push((targetX + startX - 2*m)**2 + (targetY - startY)**2);
        if(!(startX === targetX && startY > targetY)) answer.push((targetX - startX)**2 + (targetY + startY)**2);
        if(!(startX === targetX && startY < targetY)) answer.push((targetX - startX)**2 + (targetY + startY - 2*n)**2);
        return Math.min(...answer);
    });
}