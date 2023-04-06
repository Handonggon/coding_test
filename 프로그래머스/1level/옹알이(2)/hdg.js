const set = new Set(["aya", "ye", "woo", "ma"]);
function solution(babbling) {
    let prev = "";
    return babbling.filter(s=>{
        let prev = "";
        return ![...s].reduce((acc, cur)=>{
            let next = acc + cur;
            if(set.has(next) && prev !== next) {
                prev = next;
                return "";
            }
            return next;
        });
    }).length;
}