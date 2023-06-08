function solution(operations) {
    var queue = new Array();
    
    operations.map(_=>{
        let [operation, num] = _.split(" ");
        switch(operation) {
            case "I" :
                queue.push(Number(num));
                break;
            case "D" :
                let index = 0;
                if(num === "1") {
                    index = queue.indexOf(Math.max(...queue))
                } else if(num === "-1") {
                    index = queue.indexOf(Math.min(...queue))
                }
                queue.splice(index, 1);
                break;
        }
    });
    if(queue.length === 0) return [0, 0]; 
    return [Math.max(...queue), Math.min(...queue)];
}