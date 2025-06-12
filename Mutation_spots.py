n=int(input('enter the length of DNA strings:'))
str1=input('enter first sequencs:').upper()
str2=input('enter second sequence:').upper()
mutation=[]
if (len(str1)!=len(str2)):
    print("Invalid Input: DNA strings must be of the same length")
else:
    for i in range (n):
        if (str1[i]!=str2[i]):
            mutation.append(i)
    print(mutation)
