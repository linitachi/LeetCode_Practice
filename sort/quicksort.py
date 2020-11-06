def quick_sort(arr):
    def aswap(a, b):
        tem = a
        a = b
        b = tem
        return a, b

    end = len(arr) - 1
    pivot = arr[end]
    change_index = end-1
    # 從後面來看，交換的位置在pivot前一個，如果碰到比pivot小的數字就不用交換，遇到大的，
    # 就跟change_index的元素做交換，並且change_index往前移動一格
    # 因為change_index在pivot前一個，所以可以保證交換後，pivot一定會比它小。
    for i in range(change_index, -1, -1):
        if arr[i] > pivot:
            arr[i], arr[change_index] = aswap(arr[i], arr[change_index])
            change_index -= 1
    # 最後在把pivot移到change_index後面一格即可分成大小兩塊。
    arr[end], arr[change_index+1] = aswap(arr[end], arr[change_index+1])

    if len(arr) != 1:
        if arr[:change_index+1] != []:
            arr[:change_index+1] = quick_sort(arr[:change_index+1])
        if arr[change_index+1 + 1:] != []:
            arr[change_index+1 + 1:] = quick_sort(arr[change_index+1 + 1:])
    return arr
