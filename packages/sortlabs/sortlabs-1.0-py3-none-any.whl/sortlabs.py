def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)

def group_arrays(arr1, arr2):
    grouped_arr = []
    for i in range(max(len(arr1), len(arr2))):
        if i < len(arr1):
            grouped_arr.append(arr1[i])
        if i < len(arr2):
            grouped_arr.append(arr2[i])
    return grouped_arr

def merge_and_sort_arrays(arr1, arr2):
    merged_arr = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_arr.append(arr1[i])
            i += 1
        else:
            merged_arr.append(arr2[j])
            j += 1
    while i < len(arr1):
        merged_arr.append(arr1[i])
        i += 1
    while j < len(arr2):
        merged_arr.append(arr2[j])
        j += 1
    return merged_arr

def find_max(arr):
    if not arr:
        return None
    max_val = arr[0]
    for x in arr[1:]:
        if x > max_val:
            max_val = x
    return max_val

def find_min(arr):
    if not arr:
        return None
    min_val = arr[0]
    for x in arr[1:]:
        if x < min_val:
            min_val = x
    return min_val

def count_occurrences(arr, element):
    count = 0
    for item in arr:
        if item == element:
            count += 1
    return count

def remove_duplicates(arr):
    return list(set(arr))

def reverse_array(arr):
    return [arr[i] for i in range(len(arr)-1, -1, -1)]

