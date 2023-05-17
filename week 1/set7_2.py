print("enter the number of queries")
q=int(input())

def catAndMouse():
    while q>0: 
        a=int(input())
        b=int(input())
        c=int(input())
        if abs((a-c))<abs((b-c)):
            print("Cat a")
        if abs((a-c))>abs((b-c)):
            print("Cat b")
        if (a-c)==(b-c):
            print("Mouse C")

catAndMouse()

