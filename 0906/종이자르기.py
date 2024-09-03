
# 가로, 세로
W, H = map(int, input().split())
# 점선 개수
N = int(input())
# 가로, 세로 길이 저장용
W_list = [0]
H_list = [0]

# 가로, 세로 길이
for _ in range(N):
    dr, point = map(int, input().split())
    if dr == 1:
        W_list.append(point)
    else:
        H_list.append(point)
# 정렬 후 마지막 점 추가
W_list.sort()
H_list.sort()
W_list.append(W)
H_list.append(H)

max_space = 0
# 모든 네모의 면적을 구하고 그 중 최대값을 저장
for i in range(len(W_list)-1):
    for j in range(len(H_list)-1):
        a = W_list[i+1]-W_list[i]
        b = H_list[j+1]-H_list[j]
        tmp = a*b
        max_space = max(max_space, tmp)

print(max_space)