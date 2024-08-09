# 학생 수를 나타내는 정수 N(1 ≤ N ≤ 1,000)과 한 방에 배정할 수 있는 최대 인원 수 K

N, K = map(int, input().split())

# room[0] = 여자, room[1] = 남자, 1~6학년까지 2X6 배열
room = [[0] * 7 for _ in range(2)]

# 학생 수 기록
for _ in range(N):
    i, j = map(int, input().split())
    room[i][j] +=1

# 방 개수
count = 0

# 수용가능한 수 만큼 방 배정
for i in range(2):
    for j in range(1,7):
        if room[i][j] % K:
            count += (room[i][j] // K) + 1
        else:
            count += room[i][j] // K

print(count)