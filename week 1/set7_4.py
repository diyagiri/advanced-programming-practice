a = input ("Enter the list of cloud number :\n").split(" ")
l = [ int(x) for x in a]
jump = 0
i  = 0
while(i<len(l)-1):
   if(l[i+2]!=1):
      i+=2
   else:
      i+=1
   jump+=1
   
print(" The number of jumps are :", jump)