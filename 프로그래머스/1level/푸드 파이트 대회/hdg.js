function solution(food) {
    let [prefix, suffix] = ["", ""];
    for(let i = 1; i < food.length; i++) {
        for(let j = 0; j < parseInt(food[i] / 2); j++) {
            prefix = prefix + String(i);
            suffix = String(i) + suffix;
        }
    }
    return prefix + "0" + suffix;
}