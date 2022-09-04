function solution(topping) {
    let N = topping.length;
    let subtotal = {left:Array(N).fill(0), right:Array(N).fill(0)};

    let set = {left:new Set(), right:new Set()};
    for(let i = 0; i < N; i++) {
        set['left'].add(topping[i]);
        set['right'].add(topping[N-i-1]);
        subtotal['left'][i] = set['left'].size;
        subtotal['right'][N-i-1] = set['right'].size;
    }
    var answer = 0;
    for(let i = 1; i < N; i++) {
        if(subtotal['left'][i-1] === subtotal['right'][i]) answer += 1;
    }
    return answer;
}