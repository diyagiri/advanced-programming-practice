def search_range(n,a,b):
    if n in range(a,b):
        print( "Number is present in given range")
    else :
        print("The number is outside the given range.")
a=int(input("Enter upper bound of range: "))
b=int(input("Enter lower bound of range: "))
n=int(input("Enter the number to be checked: "))
search_range(n,a,b)