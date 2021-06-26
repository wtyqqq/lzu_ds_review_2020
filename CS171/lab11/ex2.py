def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):

        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


def median(list1, list2):
    for i in list2:
        list1.append(i)
    length = len(list1)
    quickSort(list1, 0, length - 1)
    if length % 2:
        return list1[int((length - 1) / 2)]
    else:
        return (list1[int(length / 2)-1] + list1[int(length / 2 + 1)-1]) / 2


if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [2, 4]
    print(median(nums1, nums2))
