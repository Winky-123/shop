Fibonacci=[1,1]
L=[]
for i in range(2,40):
    x=Fibonacci[i-1]+Fibonacci[i-2]
    Fibonacci.append(x)
for i in range(1,40):
    y=Fibonacci[i-1]/Fibonacci[i]
    L.append(y)  
print("斐波那契数列前40项："+str(Fibonacci)+"\n")
print("前一项与后一项的比值："+str(L))
