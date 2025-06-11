Size = int(input("Enter the size of List: "))
List = []
Unique_List = []
for i in range(Size):
    Temp = input(f"Enter the Integer Value at {i} Index position: ")
    lower = Temp.lower()  
    List.append(lower)
print(f"User Entered List: {List}")
for i in List:
    if i not in Unique_List:
        Unique_List.append(i)
print(f"Unique_List: {Unique_List}")

