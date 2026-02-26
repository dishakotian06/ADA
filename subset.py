def subset_sum(arr, target):
    n = len(arr)
    for i in range( 1<<n ):
        subset = []
        total = 0
        for j in range (n):
            if i & ( 1<<j ):
                subset.append(arr[j])
                total += arr[j]
        if total == target :
            print("Subset found: ", subset)
            return
        print("Subset not found ")

arr = [2, 3, 7, 5, 6]
target = 9
subset_sum(arr, target)