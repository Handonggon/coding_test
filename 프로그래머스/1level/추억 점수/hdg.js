function solution(name, yearning, photo) {
    let point = name.map((n, i)=>[n, yearning[i]]).reduce((obj, [k, v])=>{
        obj[k] = v;
        return obj;
    }, {});
    return photo.map(p=>p.map(name=>point[name] ? point[name] : 0).reduce((a, b)=>a + b));
}