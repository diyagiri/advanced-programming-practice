from functools import *
p1=[int(x) for x in input("Enter the runs scored by player 1:").split(" ")]
p2=[int(x) for x in input(f"Enter the runs scored by player 2 in {len(p1)} matches:").split(" ")]
avg1=int(reduce(lambda x,y:x+y,p1))
avg2=int(reduce(lambda x,y:x+y,p2))
if((avg1/len(p1))>(avg2/len(p2))):
   print(f"Player 1 has better average score than player 2 after {len(p1)} matches")
elif((avg1/len(p1))<(avg2/len(p2))):
    print(f"Player 2 has better average score than player 2 after {len(p1)} matches ")
else:
    print(f"Both players have same average score after {len(p1)} matches")