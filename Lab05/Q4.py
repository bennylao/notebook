def insertion_sort(nums):
    for i in range(1, len(nums)):
        t = i
        j = i - 1
        while j >= 0 and nums[t] < nums[j]:
            temp = nums[t]
            nums[t] = nums[j]
            nums[j] = temp
            t = j
            j -= 1

    return nums


def merge_sort(nums):
    if len(nums) == 1:
        return nums
    else:
        half = len(nums) // 2
        u = merge_sort(nums[:half])
        v = merge_sort(nums[half:])
        return merge(u, v)


def merge(array1, array2):
    resultant_array = []
    i = 0
    j = 0
    while i + j < len(array1) + len(array2):
        if array1[i] < array2[j]:
            resultant_array.append(array1[i])
            i += 1
        else:
            resultant_array.append(array2[j])
            j += 1
        if i >= len(array1):
            for temp in range(j, len(array2)):
                resultant_array.append(array2[temp])
            break
        if j >= len(array2):
            for temp in range(i, len(array1)):
                resultant_array.append(array1[temp])
            break

    return resultant_array


if __name__ == "__main__":
    unsorted_list = [3, 1, 5, 4, 6, 7, 9, 8, 7]
    # resultant_list = insertion_sort(unsorted_list)
    resultant_list = merge_sort(unsorted_list)
    print(resultant_list)
