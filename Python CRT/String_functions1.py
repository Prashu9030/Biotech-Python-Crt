

print(f"User entered String : {Str}")
print(f"CHecking if the  string is strts with 'p' :",s.startswith('p'))
print(f"CHecking if the  string is ends with 'ing' :",s.endswith('ing'))
print(f"Index of 'a' in the string :",s.index('a'))
print(f"Count of 'm' in the string :",s.count('m'))
print(f"Replacing 'p' with 'j' in the string :",s.replace('p','j'))
print(f"Checking the String contains Numeric :",s.isnumeric())
v=any(c in 'aeiou' for c in s)
print(f"Checking the string contains Vowels :",s.count('vowels'))
print(f"Checking the sting contains special Characters :")
Str=input("Enter the String :")
s=Str.lower()