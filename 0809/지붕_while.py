'''
주어진 정보를 통해 배열을 새로 만듬
인덱스 연산을 이용해서 품
가장 큰 값 기준으로 왼쪽 확인해서 면적 더함
오른쪽 확인해서 면적 더함
가장 큰 값이 차지하는 면적을 더함
'''
'''
7
2 4
11 4
15 8
4 6
5 3
8 10
13 6
'''
T = int(input())

arr = []
for _ in range(T):
    arr.append(list(map(int, input().split())))

arr.sort()

#  최대일때 인덱스 위치
max_idx = 0
for i in range(len(arr)):
    if arr[max_idx][1] < arr[i][1]:
        max_idx = i
max_idx_dummy = max_idx

'''
[[2, 4], [4, 6], [5, 3], [8, 10], [11, 4], [13, 6], [15, 8]]
3
'''
# 면적
box = 0
# 왼쪽 계산
left_idx = max_idx - 1
left_high_idx = max_idx - 1
# left_idx 시작값 = 2
while left_idx > -1:
    # 초기 i 값 = 2, 1, 0
    for i in range(left_idx, -1, -1):
        if arr[i][1] >= arr[left_high_idx][1]:
            left_high_idx = i
            # 가로 곱하기 세로
    box += (arr[max_idx_dummy][0] - arr[left_high_idx][0]) * arr[left_high_idx][1]
    # 왼쪽 최대 idx 변경
    max_idx_dummy = left_high_idx
    # 더 왼쪽 탐색
    left_high_idx -= 1
    left_idx = left_high_idx

max_idx_dummy = max_idx
# 오른쪽 계산
right_idx = max_idx + 1
right_high_idx = max_idx + 1
# right_idx 시작값 = 4
while right_idx < len(arr):
    # 초기 i 값 = 4, 5, 6
    for i in range(right_idx, len(arr)):
        if arr[i][1] >= arr[right_high_idx][1]:
            right_high_idx = i
            # 가로 곱하기 세로
    box += (arr[right_high_idx][0] - arr[max_idx_dummy][0]) * arr[right_high_idx][1]
    # 오른쪽 최대 idx 변경
    max_idx_dummy = right_high_idx
    # 더 오른쪽 탐색
    right_high_idx += 1
    right_idx = right_high_idx

# 가장 큰 지점 면적 더하기
box += arr[max_idx][1]


print(box)
