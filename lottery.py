import random
number=int(input("Enter a three digit number: "))
lott=random.randint(100,999)
lott1=lott%100
lott2=lott%100/10
lott3=lott/100
num1=number%100
num2=number%100/10
num3=number/100
print("The lottery number is ",lott)
if(number==lott):
    print("$10,000 won, lottery is ",lott)
elif(lott1==num2 and lott2==num3 and lott3==num1):

    print("Matched all numbers, $3000 prize")
elif(lott1==num1 or lott1==num2 or lott1==num3 or lott2==num1 or lott2==num2 or lott2==num3 or lott3==num1 or lott3==num2 or lott3==num3):

    print("Mtached one number,the award is: $1000 ")
else:

    print("Did not win any money")