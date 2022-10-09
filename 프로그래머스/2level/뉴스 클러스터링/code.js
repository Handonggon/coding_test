function solution(str1, str2) {
    str1 = str1.toUpperCase();
    str2 = str2.toUpperCase();
    const set1 = Array(str1.length-1).fill()
                                     .map((_,i)=>str1[i]+str1[i+1])
                                     .filter(_=>_.replace(/[^a-zA-Z]/g, "").length == 2);
    const map1 = {};
    for(let i = 0; i < set1.length; i++) {
        if(!map1[set1[i]]) map1[set1[i]] = 0;
        map1[set1[i]] = map1[set1[i]] + 1;
    }
    let key1 = Object.keys(map1);

    const set2 = Array(str2.length-1).fill()
                                     .map((_,i)=>str2[i]+str2[i+1])
                                     .filter(_=>_.replace(/[^a-zA-Z]/g, "").length == 2);
    const map2 = {};
    for(let i = 0; i < set2.length; i++) {
        if(!map2[set2[i]]) map2[set2[i]] = 0;
        map2[set2[i]] = map2[set2[i]] + 1;
    }
    let key2 = Object.keys(map2);

    let intersection = {};
    for(let key of key1) {
        if(key2.includes(key)) {
            intersection[key] = Math.min(map1[key], map2[key]);
        }
    }
    for(let key of key2) {
        if(key1.includes(key)) {
            intersection[key] = Math.min(map1[key], map2[key]);
        }
    }
    
    let union = {};
    for(let key of key1) {
        union[key] = map1[key];
    }
    for(let key of key2) {
        if(union[key]) union[key] = Math.max(union[key], map2[key]);
        else union[key] = map2[key];
    }
    let A = 0;
    for(let key in intersection) {
        A += intersection[key];
    }
    let B = 0;
    for(let key in union) {
        B += union[key];
    }
    
    if(B === 0) return 65536;
    return Math.floor(A/B*65536);
}