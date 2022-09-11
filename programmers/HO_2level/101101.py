from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)

    return right_index - left_index

a = [1,2,3,3,3,3,4,4,8,9,10,11]

print(count_by_range(a, 4, 4))

print(count_by_range(a, -3, -1))



def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end)



def binary_search_2(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        
        if array[mid] == target:
            return mid

        elif array[mid] > target:
            end = mid - 1

        else:
            start = mid + 1

    return None