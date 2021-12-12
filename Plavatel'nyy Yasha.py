N=int(input())
M=int(input())
x=int(input())
y=int(input())
if N>M:
    N, M = M, N
    if x>=N/2:
        x = N-x
        if y>=M/2:
            y = M-y
            if x>y:
                print(y)
            else:
                print(x)
        elif x>y:
            print(y)
        else:
            print(x)
    elif y>=M/2:
        y = M-y
        if x>y:
            print(y)
        else:
            print(x)
    elif x>y:
        print(y)
    else:
        print(x)            
elif M>N:
    if x>=N/2:
        x = N-x
        if y>=M/2:
            y = M-y
            if x>y:
                print(y)
            else:
                print(x)
        elif x>y:
            print(y)
        else:
            print(x)
    elif y>=M/2:
        y = M-y
        if x>y:
            print(y)
        else:
            print(x)
    elif x>y:
        print(y)
    else:
        print(x)


