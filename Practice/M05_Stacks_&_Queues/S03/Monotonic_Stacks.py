








def monotonic_Increasing(arr):
    stack = []
    for num in arr:
        while stack and stack[-1] > num:
            stack.pop()
        stack.append(num)
    return stack
arr =[12,21,76,2,5]
print(monotonic_Increasing(arr))





def monotonic_decreasing(arr):
    stack = []
    for num in arr:
        while stack and stack[-1] < num:
            stack.pop()
        stack.append(num)
    return stack
arr =[12,21,76,2,5]
print(monotonic_decreasing(arr))







def next_greater(arr):
    n = len(arr)
    res = [-1] * n
    for i in range(n):
        for j in range(i+1,n):
            if arr[j] > arr[i]:
                res[i] = arr[j]
                break
    return res
arr = [2,1,5,3,4]
print(next_greater(arr))


def next_greater2(arr):
    n = len(arr)
    res = [-1] * n
    stack =[]
    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            index = stack.pop()
            res[index] = arr[i]
        stack.append(i)
    return res
arr = [2,1,5,3,4]
print(next_greater2(arr))





def next_smaller(arr):
    n = len(arr)
    res = [-1] * n
    stack =[]
    for i in range(n):
        while stack and arr[stack[-1]] > arr[i]:
            index = stack.pop()
            res[index] = arr[i]
        stack.append(i)
    return res
arr = [2,1,5,3,4]
print(next_smaller(arr))



def prev_greater(arr):
    n = len(arr)
    res = [-1] * n
    stack =[]
    for i in range(n):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        if stack:
            res[i] = arr[stack[-1]]
        stack.append(i)
    return res
arr = [2,1,5,3,4]
print(prev_greater(arr))