N,K = input().split(" ")
N = int(N)
K = int(K)

list_n = []

for i in range(N):
    list_n.append(input().split(" "))

for i in list_n:
    for k in range(K):
        pixel = ""
        for j in range(len(i)):
            if j != len(i)-1:
                for m in range(K):
                    pixel += str(i[j])
                    pixel += " "
            else:
                pixel += str(i[j])
                for m in range(K-1):
                    pixel += " "
                    pixel += str(i[j])
        print(pixel)