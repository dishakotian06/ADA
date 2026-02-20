import random
import time
import matplotlib.pyplot as plt

start_time = time.time()

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
               min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr
n_list = [5000, 6000, 7000, 8000, 9000,10000]
sort_time = []
for n in n_list:
    arr =[random.randint(1,100) for _ in range(n)]
    s_t = time.time()
    selection_sort(arr)
    e_t = time.time()
    sort_time.append(e_t - s_t)

plt.plot(n_list,sort_time, marker = 'x')
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time Taken (second) ")
plt.title("Selection Sort: Time Complexity Analysis")
plt.grid(True)

plt.savefig("Selection_sort_time_complexity.png", dpi = 300, bbox_inches= 'tight')
plt.show()