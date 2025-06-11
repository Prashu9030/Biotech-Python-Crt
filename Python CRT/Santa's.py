Santa_sleigh=[]
print("Welcome to the Santa's sleigh Packing")
while(True):
    print("*****Menu*****")
    print("1,enter 1 to add a toy")
    print("2.enter 2 to List of Toy")
    print("3.enter 3 to Remove Duplicates")
    print("4.enter 4 to Sort and Print List")
    Choice=int(input("Enter the Choice :"))
    if(Choice>=1 and Choice<=4):
        if(Choice==1):
            Name=input("Enter the Toy Name :")
            Santa_sleigh.append(Name)
            print(f"{Name} is added to the Toy's List")
        elif(Choice==2):
            print("Here is the Toys list")
            print(Santa_sleigh)
        elif(Choice==3):
            unique=list(set(Santa_sleigh))
            print(f"{unique} duplicates are removed")
        elif(Choice==4):
            unique.sort()
            print("Here is the Finalised List")
            print(unique)
    else:
        print("Santa Packing")
        break
