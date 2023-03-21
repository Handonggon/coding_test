function solution(n, m, section) {
    const COUNT = 1;
    return section.reduce(([prev, count], curr)=>{
        if(prev + m > curr) return [prev, count];
        return [curr, count + 1];
    }, [-m, 0])[COUNT];
}