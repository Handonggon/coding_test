const gcd = (a, b) => a % b === 0 ? b : gcd(b, a % b);

function solution(arrayA, arrayB) {
    let a1 = arrayA.reduce((acc, cur)=>gcd(acc, cur));
    let a2 = arrayB.reduce((acc, cur)=>gcd(acc, cur));
    return Math.max((arrayA.every(num=>num%a2) ? a2 : 0), (arrayB.every(num=>num%a1) ? a1 :0));
}