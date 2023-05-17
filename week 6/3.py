import random
n=int(input("Enter the number of tickets:"))
def randint():
    l=[random.randint(100,1000) for i in range(1,n)]
    def randnum():
        return random.randint(0,n)
    return l[randnum()]
print(randint())