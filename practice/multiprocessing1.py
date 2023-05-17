import multiprocessing as mp
import threading
import time
results=[]
def How_many_in_range(row,maximum=30,minimum=5):
    for n in row:
        if minimum<=n<=maximum:
            results.append(n)
    return results
l  = [[3,11,24,17],[14,34,21,11],[15,33,13,27]]
pool=mp.Pool(mp.cpu_count())
for row in l:
    pool.apply_async(How_many_in_range,args=(row))
pool.close()
pool.join()   
print(results) 