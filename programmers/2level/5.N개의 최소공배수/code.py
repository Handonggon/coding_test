def solution(arr):
    arr.sort()
    for i in range(len(arr)-1):
        a=arr[i]
        b=arr[i+1]
        while arr[i]!=arr[i+1]:
            if arr[i] < arr[i+1]:
                arr[i] += a
            else:
                arr[i+1] +=b
    return arr[-1]
        