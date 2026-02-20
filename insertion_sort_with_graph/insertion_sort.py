import random 
import time
import matplotlib.pyplot as plt

def insertion_sort(arr):
    for i in range (1,len(arr)):
        n = arr[i]
        j = i-1
        while j>=0 and arr[j] > n:
            arr[j+1] = arr[j]
            j -= 1
            arr[j+1] = n
    return arr

#arr =  [45, 64, 89, 21, 9, 6, 13, 0, 3, 2]
#print(insertion_sort(arr))
n_list = [5000, 6000, 7000, 8000, 9000,10000]
sort_time = []
for n in n_list:
    arr =[random.randint(1,100) for _ in range(n)]
    s_t = time.time()
    insertion_sort(arr)
    e_t = time.time()
    sort_time.append(e_t - s_t)

#print(n_list)
#print(sort_time)

plt.plot(n_list,sort_time, marker = 'x')
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time Taken (second) ")
plt.title("Insertion sort Sort: Time Complexity Analysis")
plt.grid(True)

plt.savefig("insertion_sort_time_complexity.png", dpi = 300, bbox_inches= 'tight')
plt.show()


 
