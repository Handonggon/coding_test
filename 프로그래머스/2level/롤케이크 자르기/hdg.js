function solution(topping) {
    let set = new Set();
    
    set.clear();
    let left = new Array(topping.length + 1).fill(0);
    for(let i = 0; i < topping.length; i++) {
        set.add(topping[i]);
        left[i + 1] = set.size;
    }
    
    set.clear();
    let right = new Array(topping.length + 1).fill(0);
    for(let i = topping.length - 1; i >= 0; i--) {
        set.add(topping[i]);
        right[i] = set.size;
    }
    
    return Array(topping.length + 1).fill(0).map((_, i)=>left[i]===right[i]).reduce((a, b)=>a + b);
}