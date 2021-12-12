n=8
x=[]
y=[]
for i in range(n):
    xk, ym=[int(s) for s in input().split()]
    x.append(xk)
    y.append(ym)
correct = True
for i in range(n):
    for j in range(i+1, n):
        if x[i]==x[j] or y[i]==y[j] or abs(x[i]-x[j])==abs(y[i]-y[j]):
            correct=False
if correct:
    print('NO')
else:
    print('YES')