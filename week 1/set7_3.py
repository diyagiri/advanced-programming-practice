def chocolateFeast(availableCash, price, wrapperDiscount):
    eaten = availableCash // price
    wraps = eaten
 
    while wraps >= wrapperDiscount:
        newlyEaten = wraps // wrapperDiscount
        eaten += newlyEaten
        wraps = wraps % wrapperDiscount + newlyEaten
    return eaten
print("Enter amount available, cost of one bar, and wrapper discount")
n = int(input())
c = int(input())
m = int(input())
print("No of bars eaten = " ,chocolateFeast(n,c,m))