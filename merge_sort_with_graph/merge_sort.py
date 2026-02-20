import random
import time
import matplotlib.pyplot as plt

def merge_sort(a):
    
    n=len(a)
    if (n>1):
        b=a[0:n//2]
        c=a[n//2:n]
        print(b,"|",c)
        merge_sort(b)
        merge_sort(c)
        merge(a,b,c)
def merge(a,b,c):
    n1=len(b)
    n2=len(c)
    i=j=k=0
    while (i<n1 and j<n2):
        if (b[i]<c[j]):
            a[k]=b[i]
            i+=1
        else:
            a[k]=c[j]
            j+=1
        k+=1
    while (i<n1):
        a[k]=b[i]
        i+=1
        k+=1
    while (j<n2):
        a[k]=c[j]
        j+=1
        k+=1
    print(a)

n_list = [5000, 6000, 7000, 8000, 9000,10000]
sort_time = []
for n in n_list:
    arr =[random.randint(1,100) for _ in range(n)]
    s_t = time.time()
    merge_sort(arr)
    e_t = time.time()
    sort_time.append(e_t - s_t)

plt.plot(n_list,sort_time, marker = 'x')
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time Taken (second) ")
plt.title("Merge Sort: Time Complexity Analysis")
plt.grid(True)

plt.savefig("merge_sort_time_complexity.png", dpi = 300, bbox_inches= 'tight')
plt.show()