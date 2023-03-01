function solution(elements) {
    let prefix = [0];
    for(let i = 0; i < (elements.length * 2) - 1; i++) {
        prefix.push(prefix[prefix.length - 1] + elements[i % elements.length])
    }
    const set = new Set();
    for(let size = 1; size <= elements.length; size++) {
        for(let i = 0; i < elements.length; i++) {
            set.add(prefix[i + size] - prefix[i]);
        }
    }
    return set.size;
}