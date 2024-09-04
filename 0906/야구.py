def get_score(arr):
    global N, max_score
    # now = 현재 이닝
    now = 0
    # nt = 현재 타자
    nt_idx = 0
    nt = arr[nt_idx]
    # 이번 게임에서 얻는 점수
    cnt = 0
    # 이닝이 N보다 작을 때
    while now < N:
        # nt = 현재 타자
        out = 0
        # 현재 필드 상황 // 1루 2루 3루
        field = [0, 0, 0]
        # 아웃이 3개 이하일때
        while out < 3:
            # 안타 2루타 3루타 홈런 아웃 4개에 대한 상황 고려

            # 아웃일때 -- 아웃 횟수 증가시키고 다음 타자로 넘어감
            if ining[now][nt-1] == 0:
                out += 1
                nt_idx = (nt_idx + 1) % 9
                nt = arr[nt_idx]

            # 안타일때 -- 타자 이동 시키고 다음 타자로 넘어감
            elif ining[now][nt-1] == 1:
                if field[2] == 1:
                    cnt += 1
                    field[2] = 0
                if field[1] == 1:
                    field[1] = 0
                    field[2] = 1
                if field[0] == 1:
                    field[0] = 0
                    field[1] = 1
                field[0] = 1
                nt_idx = (nt_idx + 1) % 9
                nt = arr[nt_idx]

            # 2루타일때 -- 타자 이동 시키고 다음 타자로 넘어감
            elif ining[now][nt-1] == 2:
                if field[2] == 1:
                    cnt += 1
                    field[2] = 0
                if field[1] == 1:
                    cnt += 1
                    field[1] = 0
                if field[0] == 1:
                    field[0] = 0
                    field[2] = 1
                field[1] = 1
                nt_idx = (nt_idx + 1) % 9
                nt = arr[nt_idx]

            # 3루타일때 -- 타자 이동 시키고 다음 타자로 넘어감
            elif ining[now][nt-1] == 3:
                if field[2] == 1:
                    cnt += 1
                    field[2] = 0
                if field[1] == 1:
                    cnt += 1
                    field[1] = 0
                if field[0] == 1:
                    cnt += 1
                    field[0] = 0
                field[2] = 1
                nt_idx = (nt_idx + 1) % 9
                nt = arr[nt_idx]

            # 홈런일때 -- 타자 이동 시키고 다음 타자로 넘어감
            elif ining[now][nt-1] == 4:
                if field[2] == 1:
                    cnt += 1
                    field[2] = 0
                if field[1] == 1:
                    cnt += 1
                    field[1] = 0
                if field[0] == 1:
                    cnt += 1
                    field[0] = 0
                cnt += 1
                nt_idx = (nt_idx + 1) % 9
                nt = arr[nt_idx]
        # 이닝 수 증가
        now += 1
    # 최대 점수 저장
    max_score = max(max_score, cnt)
    return

# 조합 만들기
def perm(arr, n):
    # 모든 숫자를 이용해 조합을 만들었다면
    if n == len(taja):
        # 1번 타자는 무조건 4번에서 치기 때문에 1번과 4번을 바꿔줌
        arr[0], arr[3] = arr[3], arr[0]
        # 점수를 계산함
        get_score(arr)
        # 다시 원상복구함
        arr[0], arr[3] = arr[3], arr[0]
        return
    # 1번 제외 나머지 8명에 대해서 구함
    for i in range(1, 9):
        # 선택하지 않은 수라면
        if used[i] == 0:
            # 선택 표시
            used[i] = 1
            # 배열에 추가함
            arr.append(taja[i])
            # 다음 조합에 올 수 찾음
            perm(arr, n+1)
            # 배열에서 꺼냄
            arr.pop()
            # 선택 표시 지움
            used[i] = 0
# 이닝 수
N = int(input())

# 각 이닝마다 공을 치는 경우
ining = [list(map(int, input().split())) for _ in range(N)]

# 한 이닝 당 점수를 가장 많이 얻을 때의
max_score = 0

# 타순을 정해야함 // 1번 타자가 4번째에 침
# x, x, x, 1, x, x, x, x, x <-- 조합 만들기 필요함
taja = [1, 2, 3, 4, 5, 6, 7, 8, 9]
used = [0] * 9
# 1번 타자는 위치가 정해져있기 때문에 제외함
used[0] = 1
perm([1], 1)
# 최대 점수 출력
print(max_score)