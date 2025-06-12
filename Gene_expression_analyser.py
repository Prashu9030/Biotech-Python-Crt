size=int(input("Enter the size of list :"))
Underexpressed=0
Normal=0
Overexpressed=0
list=[]
res=[]
for i in range(size):
    gene=float(input("Enter the gene Expression Value :"))
    list.append(gene)
    if gene<5:
        res.append("Underexpressed")
    elif(gene>=5 and i<=15):
        res.append("Normal")
    else:
        res.append("Overexpressed")
print("User Entered List :",list)
print(res)
     