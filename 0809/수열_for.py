T = int(input())

arr = list(map(int, input().split()))

# count = 현재 길이, max_length = 최대 길이
count = 1
max_length = 1

# 증가하는 경우
for i in range(1, T):
    if arr[i] >= arr[i-1]:
        count += 1
    else:
        if count > max_length:
            max_length = count
        count = 1

if count > max_length:
    max_length = count

# 초기화
count = 1

# 감소하는 경우
for i in range(1, T):
    if arr[i] <= arr[i - 1]:
        count += 1
    else:
        if count > max_length:
            max_length = count
        count = 1

if count > max_length:
    max_length = count

print(max_length)