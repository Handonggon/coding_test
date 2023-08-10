import sys
input = sys.stdin.readline

N = int(input())
tree = {}
for _ in range(N):
    [p, c1, c2] = input().split()
    tree[p] = [c1, c2]

def preOrder(p):
    return p + preOrder(tree[p][0]) + preOrder(tree[p][1]) if p in tree else ""

def inOrder(p):
    return inOrder(tree[p][0]) + p + inOrder(tree[p][1]) if p in tree else ""

def postOrder(p):
    return postOrder(tree[p][0]) + postOrder(tree[p][1]) + p if p in tree else ""

print(preOrder('A'))
print(inOrder('A'))
print(postOrder('A'))