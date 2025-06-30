num=int(input("enter a number"))
original=num
rev=0
while num>0:
    digit=num%10# while look ki 3 line logic hai palendrome num. ka:
    rev=rev*10+ digit
    num=num//10
if original== rev:
    print(f"{original}is a palindrome")
else:
    print(f"{original}is not a palindrome")