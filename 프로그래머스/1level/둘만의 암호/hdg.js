function solution(s, skip, index) {
    let alphabet = [...Array(26).keys()].map(key=>String.fromCharCode(key + 'a'.charCodeAt(0)));
    let decryption = {};
    for(let i = 0; i < alphabet.length; i++) {
        let origin = alphabet[i];
        
        let count = 0;
        for(let j = i; true; j = (j + 1) % alphabet.length) {
            let target = alphabet[j];
            if(skip.includes(target)) continue;
            if(count >= index) {
                decryption[origin] = target;
                break;
            }
            count++;
        }
    }
    return [...s].map(c=>decryption[c]).join("");
}