T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    arr = [list(map(int, input())) for _ in range(N)]

    '''
    제일 위부터 좌우 1칸씩 넓어지다가 중간에 도달하면 그 이후부터 좌우 1칸씩 줄어들음
    다이아몬드 모양으로 농작물을 수확함
    중앙에서 좌우 1칸씩 늘려나가는 방법을 사용하다가 중앙에 도달하면 그 이후부터 좌우 1칸씩 줄임
    '''
    # 저장용 배열
    summ = 0
    # 시작, 끝 지점
    start, end = N // 2, N // 2
    # 위부분
    for i in range(N // 2):
        for j in range(start, end + 1):
            summ += arr[i][j]
        start -= 1
        end += 1

    # 중간, 아래부분
    for i in range(N // 2, N):
        for j in range(start, end + 1):
            summ += arr[i][j]
        start += 1
        end -= 1

    print(f'#{test_case} {summ}')
