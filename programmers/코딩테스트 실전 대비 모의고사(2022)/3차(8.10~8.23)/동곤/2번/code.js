const INGREDIENT = ["", "BREAD", "VEGETABLE", "MEAT"];
const RECIPE = [1, 3, 2, 1];

function solution(ingredients) {
    let answer = 0;

    let stack = [];
    for(let ingredient of ingredients) {
        stack.push(ingredient);
        if(INGREDIENT[ingredient] === "BREAD" && stack.length >= RECIPE.length) {
            let complete = true;
            for(let index = 0; index < RECIPE.length; index++) {
                if(stack[stack.length-1-index]!==RECIPE[index]) {
                    complete = false;
                    break;
                }
            }
            if(complete) {
                for(let index = 0; index < RECIPE.length; index++) stack.pop();
                answer += 1;
            }
        }
    }
    return answer;
}