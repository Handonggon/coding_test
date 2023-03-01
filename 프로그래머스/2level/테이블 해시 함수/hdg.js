function solution(data, col, row_begin, row_end) {
    return data.sort((a, b)=>((a[col - 1] === b[col - 1]) ? (b[0] - a[0]) : (a[col - 1] - b[col - 1])))
               .map((tuple, i)=>tuple.reduce((acc, cur)=>acc + (cur % (i + 1)), 0))
               .filter((_, i)=>(row_begin - 1) <= i && i <= (row_end - 1))
               .reduce((acc, cur)=>acc ^ cur);
}