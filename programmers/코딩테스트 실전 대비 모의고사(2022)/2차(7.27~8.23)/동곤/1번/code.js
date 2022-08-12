function solution(number) {
    function combination(arr, selectNum) {
        const result = [];
        if (selectNum === 1) return arr.map((v) => [v]);
        arr.forEach((v, idx, arr) => {
            const fixed = v;
            const restArr = arr.slice(idx + 1);
            const combinationArr = combination(restArr, selectNum - 1);
            const combineFix = combinationArr.map((v) => [fixed, ...v]);
            result.push(...combineFix);
        });
        return result;
    }
    return combination(number, 3).map(com=>com.reduce((a,b)=>a+b)).filter(sum=>sum===0).length;
}