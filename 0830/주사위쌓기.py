# def sum_dice(top, bottom, d, idx):
#     global max_dice, N
#     # 모든 주사위 다 봤으면
#     if idx > N-2:
#         max_dice = max(max_dice, d)
#         return
#     if max_dice > 6*(N-idx-1) + d:
#         return
#     # 현재 주사위의 바닥면 찾음
#     bottom_idx = 0
#     for i in range(6):
#         if rest[idx][i] == top:
#             bottom_idx = i
#             break
#
#     # 현재 주사위의 윗면 찾음
#     if bottom_idx == 0:
#         top_idx = 5
#     elif bottom_idx == 1:
#         top_idx = 3
#     elif bottom_idx == 2:
#         top_idx = 4
#     elif bottom_idx == 3:
#         top_idx = 1
#     elif bottom_idx == 4:
#         top_idx = 2
#     elif bottom_idx == 5:
#         top_idx = 1
#
#     # 윗면, 바닥면 제외 나머지 4개 중 최댓값 찾음
#     tmp = []
#     for j in range(6):
#         if j != bottom_idx and j != top_idx:
#             tmp.append(rest[idx][j])
#     d += max(tmp)
#
#     # 다음 주사위 계산함
#     sum_dice(rest[idx][top_idx], rest[idx][bottom_idx], d, idx+1)
#     return

def sum_dice(top, d, idx):
    global max_dice, N
    # 남은 주사위들 중에서
    for k in range(N-1):
        # 현재 주사위의 바닥면 찾음
        bottom_idx = 0
        for i in range(6):
            if rest[idx][i] == top:
                bottom_idx = i
                break
        # 현재 주사위의 윗면 찾음
        if bottom_idx == 0:
            top_idx = 5
        elif bottom_idx == 1:
            top_idx = 3
        elif bottom_idx == 2:
            top_idx = 4
        elif bottom_idx == 3:
            top_idx = 1
        elif bottom_idx == 4:
            top_idx = 2
        elif bottom_idx == 5:
            top_idx = 0
        top = rest[idx][top_idx]
        # 윗면, 바닥면 제외 나머지 4개 중 최댓값 찾음
        tmp = []
        for j in range(6):
            if j != bottom_idx and j != top_idx:
                tmp.append(rest[idx][j])
        d += max(tmp)
        idx += 1
    max_dice = max(max_dice, d)
    return



# 주사위 개수
N = int(input())

# 첫번째 주사위 찾음
first = list(map(int, input().split()))
# 남은 주사위는 N-1개
rest = [list(map(int, input().split())) for _ in range(N-1)]


max_dice = 0
# 첫번째 주사위는 모든 경우의 수 고려 필요함
for i in range(6):
    if i == 0:
        top = first[0]
        d = (max(first[1], first[2], first[3], first[4]))
        sum_dice(top, d, 0)
    elif i == 1:
        top = first[1]
        d = (max(first[0], first[2], first[4], first[5]))
        sum_dice(top, d, 0)
    elif i == 2:
        top = first[2]
        d = (max(first[0], first[1], first[3], first[5]))
        sum_dice(top, d, 0)
    elif i == 3:
        top = first[3]
        d = (max(first[0], first[2], first[4], first[5]))
        sum_dice(top, d, 0)
    elif i == 4:
        top = first[4]
        d = (max(first[0], first[1], first[3], first[5]))
        sum_dice(top, d, 0)
    elif i == 5:
        top = first[5]
        d = (max(first[1], first[2], first[3], first[4]))
        sum_dice(top, d, 0)

print(max_dice)


