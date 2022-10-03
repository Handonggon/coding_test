T = input()

for t in range(int(T)): 
    N = input()
    c= []
    g= []
    for i in range(int(N)):
        CG = input().split(" ")
        c.append(int(CG[0]))
        g.append(float(CG[1])) 

    sumc = sum(c)
    sumg = 0
    for i in range(len(c)):
        sumg += g[i]*(c[i]/sumc)


    print(sumc,sumg)