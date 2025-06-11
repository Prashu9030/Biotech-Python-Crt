IPL_List=['csk','Rcb','SRH','GT']
print("Accesing List Elements Without Index :")
for i in IPL_List:
    print(i)
print("Accessing List Elements With Index Using while loop :")
i=0
while(i<len(IPL_List)):
    print(IPL_List[i])
    i+=1
print("Accessing List Elements With Index")
for i in range(3):
    print(IPL_List[i])