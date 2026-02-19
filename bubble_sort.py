import random
import time

n=1000
l = [random.randint(1,1000) for _ in range(n)]
start_time = time.time() 

def bubble_sort(arr):
    n = len(l)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if l[j+1] < l[j]:
                l[j], l[j+1] = l[j+1], l[j]
    return l
end_time = time.time()
print(bubble_sort(l))
print("Execution time: ", end_time - start_time ,"seconds" )

