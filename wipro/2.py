min= -32767
 
def cutRod(p, n):
    val = [0 for x in range(n+1)]
    val[0] = 0
 
    for i in range(1, n+1):
        max_val = min
        for j in range(i):
             max_val = max(max_val, p[j] + val[i-j-1])
        val[i] = max_val
 
    return val[n]
 
arr = [8,3,5,8,9,10,17,17,20]
size = len(arr)
print("Maximum Obtainable Value is " + str(cutRod(arr, size)))