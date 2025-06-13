def prime(num):
    count=0
    for i in range(2,num//2+ 1):
        if num % i == 0:
            count += 1
    if count == 0:
        print(f"{num} is a Prime Number")
    else:
        print(f"{num} is not a Prime Number")
prime(num=int(input("Enter a number to check Prime or Not : ")))


#method 2

def prime(num):
    count=0
    for i in range(1,num+ 1):
        if num % i == 0:
            count += 1
    if count == 2:
        print(f"{num} is a Prime Number")
    else:
        print(f"{num} is not a Prime Number")
prime(num=int(input("Enter a number to check Prime or Not : ")))
