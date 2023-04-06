const [BREAD, LEAF, MEAT] = [1, 2, 3];
const RECIPE = [BREAD
              , MEAT
              , LEAF
              , BREAD];

function solution(ingredients) {
    let answer = 0;
    let stack = [];
    for(let ingredient of ingredients) {
        stack.push(ingredient);
        while(stack.length >= RECIPE.length) {
            let isPackaging = true;
            for(let i = 0; i < RECIPE.length; i++) {
                if(RECIPE[i] === stack[stack.length - 1 - i]) continue;
                isPackaging = false;
                break;
            }
            if(isPackaging) {
                for(let i = 0; i < RECIPE.length; i++) stack.pop();
                answer += 1
            } else {
                break;
            }
        }
    }
    return answer;
}