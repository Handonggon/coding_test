function solution(keymap, targets) {
    keymap = keymap.map(key=>[...key].map((str, index)=>[str, index + 1])).flat().reduce((obj, [str, index])=>{
        obj[str] = Math.min(index, obj.hasOwnProperty(str) ? obj[str] : index);
        return obj;
    }, {});
    return targets.map((target, index)=>{
        let answer = 0;
        for(let str of target) {
            if(!keymap.hasOwnProperty(str)) return -1;
            answer += keymap[str];
        }
        return answer;
    });
}