const INGREDIENT = {BREAD: 1, VEGETABLE: 2, MEAT: 3};
const RECIPE = [INGREDIENT.BREAD
              , INGREDIENT.MEAT
              , INGREDIENT.VEGETABLE
              , INGREDIENT.BREAD];

function solution(ingredients) {
    let answer = 0;

    let stack = [];
    for(let ingredient of ingredients) {
        stack.push(ingredient);
        if(ingredient === INGREDIENT.BREAD && stack.length >= RECIPE.length) {
            let complete = true;
            for(let index = 0; index < RECIPE.length; index++) {
                if(stack[stack.length-(index+1)] === RECIPE[index]) continue;
                complete = false;
                break;
            }
            if(complete) {
                for(let index = 0; index < RECIPE.length; index++) stack.pop();
                answer += 1;
            }
        }
    }
    return answer;
}