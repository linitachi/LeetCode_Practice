def bubble_sort(arr):
    def swap(a, b):
        tem = a
        a = b
        b = tem
        return a, b

    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = swap(arr[i], arr[j])
    return arr
