num=int(input("enter a number"))
original=num
sum=0
while num>0:
    digit = num%10
    sum=sum+(digit**3)
    num=num//10
if original==sum:
    print(f"{original}is an Armstring number")
else:
    print(f"{original}is not an Armstrong number")


    #153 is a Armstorng number:
    #kyuki 1 and 5 and 3 ka quebe karke add karne pr 153 hi aata hai
    