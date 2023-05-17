prisoner=int(input("Enter number of Prisoners : "))
candy=int(input("Enter the number of Candy : "))
start=int(input("Enter the starting postition : "))
position=-1
if(candy<prisoner-start):
    position=start+candy-1
else:
    buffer=prisoner-start 
    left=candy%prisoner 
    
    if(left<=buffer):
        position=start+left - 1
        print(1)
    else:
        position=left - buffer -1
        print(2)
print("The Prisoner to be warned is : ",position)