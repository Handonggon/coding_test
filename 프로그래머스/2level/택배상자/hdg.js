function solution(order) {
    let truck = [];
    let container = [];
    let box = 1;
    let index = 0;
    while(truck.length !== order.length) {
        if(order[index] === box) {
            truck.push(box);
            box += 1;
            index += 1;
        } else {
            if(order[index] === container[container.length-1]) {
                truck.push(container.pop());
                index += 1;
            } else {
                if(box > order.length) break;
                container.push(box);
                box += 1;
            }
        }
    }
    return index;
}