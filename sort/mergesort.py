def merge_sort(arr):
    def divide(arr):
        # 分割成兩部分
        arr[: len(arr) // 2] = merge_sort(arr[: len(arr) // 2])
        arr[len(arr) // 2:] = merge_sort(arr[len(arr) // 2:])
        return arr[: len(arr) // 2],  arr[len(arr) // 2:]

    def merge(arr1, arr2):
        # 合併起來
        if arr1 == []:
            return arr2
        if arr2 == []:
            return arr1

        index_arr1 = 0
        index_arr2 = 0
        arr = []
        while index_arr1 != len(arr1) and index_arr2 != len(arr2):
            if arr1[index_arr1] > arr2[index_arr2]:
                arr.append(arr2[index_arr2])
                index_arr2 += 1
            else:
                arr.append(arr1[index_arr1])
                index_arr1 += 1
        if index_arr2 != len(arr2):
            arr.extend(arr2[index_arr2:])
        if index_arr1 != len(arr1):
            arr.extend(arr1[index_arr1:])
        return arr

    if len(arr) != 1:
        arr[: len(arr) // 2], arr[len(arr) // 2:] = divide(arr)
    arr = merge(arr[: len(arr) // 2], arr[len(arr) // 2:])
    return arr
