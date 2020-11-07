# 把第i筆資料，插進已經排序好的數列裡面
def insertion_sort(arr):
    def insert(arr, i):
        for index in range(i):  # 找到對應的位置插進去
            if arr[index] > arr[i]:
                tem = arr[index]
                arr[index] = arr[i]
                for j in range(index + 1, i + 1):  # 把插進去的位置後面的元素都後移一格。
                    tem2 = arr[j]
                    arr[j] = tem
                    tem = tem2
                break
        return arr

    for i in range(len(arr)):
        arr = insert(arr, i)
    return arr
