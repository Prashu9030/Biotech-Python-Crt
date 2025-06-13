def Arthmetic():
    c=x+y
    return "Addition:{c} \nSubtraction:{d} \nMultiplication:{e} \nDivision:{f}".format(c=c, d=x-y, e=x*y, f=x/y)
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
res=Arthmetic()
print(Arthmetic())