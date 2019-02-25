def sort(arr):
    if len(arr)<=1:
        return arr
    left_arr = []
    right_arr = []
    mid = arr.pop()
    for item in arr:
        if item >= mid:
            right_arr.append(item)
        else:
            left_arr.append(item)
    return sort(left_arr) + [mid] + sort(right_arr)


arr = [9,8,7,6,5,4,3,2,1,1,2,3,4,5,6,7,8,9,9]
print(sort(arr))