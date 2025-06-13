def reverse(n):
    count=0
    for i in range(1,n+1):
        if n % i == 0:
            count += 1
    if count == 2:
        return "Prime Palindrome Number " if n == n[::-1] else "Not a Prime Palindrome Number"
reverse(n=int(input("Enter a number to check Prime Palindrome or Not : " )))
