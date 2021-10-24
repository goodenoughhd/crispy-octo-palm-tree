x=int(input())
n=summ_squares=summ=0
while x!=0:
    n+=1
    summ+=x
    summ_squares+=x**2
    x=int(input())
print(((summ_squares-summ**2/n)/(n-1))**0.5)
 