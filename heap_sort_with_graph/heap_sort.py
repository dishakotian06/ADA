import random 
import time
import matplotlib.pyplot as plt

def max_heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)


def heapsort(arr):
    n = len(arr)

   
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)

    
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        max_heapify(arr, i, 0)

    return arr


if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", data)
    print("Sorted array:", heapsort(data.copy()))

n_list = [5000, 6000, 7000, 8000, 9000,10000]
sort_time = []
for n in n_list:
    arr =[random.randint(1,100) for _ in range(n)]
    s_t = time.time()
    heapsort(arr)
    e_t = time.time()
    sort_time.append(e_t - s_t)

plt.plot(n_list,sort_time, marker = 'x')
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time Taken (second) ")
plt.title("Heap Sort: Time Complexity Analysis")
plt.grid(True)

plt.savefig("Heap_sort_time_complexity.png", dpi = 300, bbox_inches= 'tight')
plt.show()
