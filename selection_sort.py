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
end_time = time.time()
n = 6000
numbers = [random.randint(1,1000) for _ in range(n)]
sorted_num = selection_sort(numbers)
#print(sorted_num)
#print("Execution time: ", end_time - start_time ,"seconds" )

plt.plot( sorted_num, numbers, marker = 'x')
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time Taken (second) ")
plt.title("Selection sort Sort: Time Complexity Analysis")
plt.grid(True)

plt.savefig("selection_sort_time_complexity.png", dpi = 300, bbox_inches= 'tight')
plt.show()
