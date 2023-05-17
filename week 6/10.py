z=[2,3,6,-1,-4,-7,8]
s=0
sum1=list(filter(lambda num:num>=0,z))
for i in range(0,len(sum1)):
    s=s+sum1[i]
print(s)