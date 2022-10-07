while True:
    try :
        N = input().split(" ")
        answer = []
        for i in N:
            answer.append(int(float(i)*1000))
        xm = answer[2]-answer[0]
        ym = answer[3]-answer[1]

        x = str(answer[6]-xm)
        y = str(answer[7]-ym)
        if int(x) >= 1000 or int(x) <=  -1000:

            rx = ""
            for i in range(1,len(x)+1):
                if i != 4:
                    rx = x[-i] + rx
                else:
                    rx = x[-i] + "." + rx
        else:
            m = ""
            if x[0] == "-":
                m += "-"
                x = x[1:]


            rx = ""
            for i in range(1,len(x)+1):
                rx = x[-i] + rx
            while len(rx) != 3:
                rx = "0" + rx
            rx = m + "0." + rx

        if int(y) >= 1000 or int(y) <=  -1000:
            ry = ""
            for i in range(1,len(y)+1):
                if i != 4:
                    ry = y[-i] + ry
                else:
                    ry = y[-i] + "." + ry
        else:
            m = ""
            if y[0] =="-":
                m += "-"
                y = y[1:]

            ry = ""
            for i in range(1,len(y)+1):
                ry = y[-i] + ry
            while len(ry) != 3:
                ry = "0" + ry
            ry = m + "0." + ry

        print(rx,ry)
    
    except EOFError:
        break