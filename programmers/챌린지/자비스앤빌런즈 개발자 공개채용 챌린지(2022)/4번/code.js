class MyStack {
    constructor(n) {
        this.root = 0;
        this.stack = Array(n).fill(0).map(_=>[]);
    }

    push(a, b) {
        if(this.root === 0) {
            this.root = b;
        } else {
            this.stack[a-1].push(b);
        }
    }
    pop(a) {
        if(this.stack[a-1].length) {
            return this.stack[a-1].pop();
        } else {
            if(this.root === 0) return -1;
            let temp = this.root;
            this.root = 0;
            let da = a%this.stack.length;
            while((a-1) !== da) {
                if(this.stack[da].length) {
                    this.root = this.stack[da].shift();
                    break;
                }
                da = (da+1)%this.stack.length;
          }
          return temp;
      }
  }
}

function solution(n, queries) {
    let myStack = new MyStack(n);
    var answer = [];
    for(let querie of queries) {
        let [a, b] = querie;
        if(b === -1) {
            answer.push(myStack.pop(a));
        } else {
            myStack.push(a, b);
        }
    }
    return answer;
}