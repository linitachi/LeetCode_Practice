def selection_sort(arr):
    def swap(a, b):
        tem = a
        a = b
        b = tem
        return a, b
    min_index = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[min_index], arr[i] = swap(arr[min_index], arr[i])
    return arr
