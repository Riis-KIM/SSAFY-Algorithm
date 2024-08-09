T = int(input())

arr = list(map(int, input().split()))

count = 1
max_length = 1
if arr[0] > arr[1]:
    flag = False
else:
    flag = True

for i in range(1, len(arr)):
    if arr[i] > arr[i-1]:
        if flag:
            count+=1
        else:
            flag = True
            if count > max_length:
                max_length = count
            count = 2

    elif arr[i] < arr[i-1]:
        if not flag:
            count+=1
        else:
            flag = False
            if count > max_length:
                max_length = count
            count = 2

    else:
        count+=1


if count > max_length:
    max_length = count


print(max_length)