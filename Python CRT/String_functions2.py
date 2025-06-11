Str=input("Enter a string: ")
digit_count=0
vowel_count=0
special_count=0
for char in Str:
    if char.isdigit():
        digit_count += 1   
    elif char.lower() in 'aeiou':
        vowel_count += 1
    elif not char.isalnum():
        special_count += 1
print(f"Number of digits in the string: {digit_count}")
print(f"Number of vowels in the string: {vowel_count}")
print(f"Number of special characters in the string: {special_count}")
