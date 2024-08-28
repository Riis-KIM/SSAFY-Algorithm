N = int(input())

arr = [list(map(int, input().split())) for _ in range(6)]

# 최대 길이
max_width = 0
max_width_idx = 0
# 최대 높이
max_height = 0
max_height_idx = 0

## 1, 2 가로 3, 4 세로
for t in range(6):
    if (arr[t][0] == 1 or arr[t][0] == 2):
        if max_width < arr[t][1]:
            max_width = arr[t][1]
            max_width_idx = t

    elif (arr[t][0] == 3 or arr[t][0] == 4):
        if max_height < arr[t][1]:
            max_height = arr[t][1]
            max_height_idx = t

# 큰 상자
big_square = max_width * max_height
# 작은 상자는 가장 큰 변의 인덱스에서 3칸 가면 작은 상자의 변이 나옴
small_square = arr[(max_width_idx+3)%6][1] * arr[(max_height_idx+3)%6][1]

ans = (big_square - small_square) * N
print(ans)