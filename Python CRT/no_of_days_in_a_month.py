n=int(input("Enter the Month Number :"))
if(n==2):
    print("28")
elif(n==4 or n==6 or n==11):
    print("30")
elif(n==1 or n==3 or n==5 or n==7 or n==8 or n==10 or n==12):
    print("31")
else:
    print("Invalid month")