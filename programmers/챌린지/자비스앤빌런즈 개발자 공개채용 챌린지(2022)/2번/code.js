function solution(orders) {
    let half = Math.ceil(orders.length / 2);

    let candidates = Array(orders.length).fill(0).map((_, index)=>orders.length-1-index);
    for(let count = 1; true; count++) {
        let favorite = candidates.reduce((obj, number)=>{
            obj[number] = 0;
            return obj;
        }, new Object());
        
        for(let order of orders) {
            for(let number of order) {
                if(!candidates.includes(number)) continue;
                favorite[number]++;
                break;
            }
        }

        
        for(let candidate of candidates) {
            if(favorite[candidate] >= half) {
                return [count, candidate];
            }
        }
        candidates.sort((a,b)=>{
            if(favorite[a] === favorite[b]) {
                return b - a;
            }
            return favorite[b] - favorite[a];
        });
        candidates.pop();
    }
}