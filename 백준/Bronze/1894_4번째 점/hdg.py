while True :
    try :
        [x1, y1, x2, y2, x3, y3, x4, y4] = list(map(float, input().split()))
        if x1 == x3 and y1 == y3:
            print("{:.3f} {:.3f}".format(x2 + x4 - x1,  y2 + y4 - y1))
        if x1 == x4 and y1 == y4:
            print("{:.3f} {:.3f}".format(x2 + x3 - x1,  y2 + y3 - y1))
        if x2 == x3 and y2 == y3:
            print("{:.3f} {:.3f}".format(x1 + x4 - x2,  y1 + y4 - y2))
        if x2 == x4 and y2 == y4:
            print("{:.3f} {:.3f}".format(x1 + x3 - x2,  y1 + y3 - y2))
    except EOFError:
        break