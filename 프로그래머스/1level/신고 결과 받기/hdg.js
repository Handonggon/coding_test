function solution(id_list, reports, k) {
    let idOfReport = {};
    for(let id of id_list) {
        idOfReport[id] = new Set();
        idOfReport[id].count = 0;
    }
    
    for(let report of reports) {
        let [report_id, use_id] = report.split(" ");
        idOfReport[use_id].add(report_id);
    }
    
    for(let id of id_list) {
        if(idOfReport[id].size >= k) {
            for(let report_id of Array.from(idOfReport[id])) {
                idOfReport[report_id].count++;
            }
        }
    }
    return Array(id_list.length).fill()
                                .map((_,index)=>idOfReport[id_list[index]].count);
}

