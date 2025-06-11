Size=int(input("Enter the range of list :"))
Num=[]
Sum=0
for i in range(Size):
    value=int(input(f"Enter the value at{i} INdex :"))
    Num.append(value)
print(f"Oringinal list : {Num}")
for i in range(Size):
    Sum+=Num[i]
print(Sum)
