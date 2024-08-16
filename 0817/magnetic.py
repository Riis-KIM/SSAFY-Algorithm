T = 10

for test_case in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(100)]

    count = 0
    '''
    모든 범위에 대해서 (세로 확인)
    자석이 어떻게 붙는지 잘 생각해야함
    N극은 무조건 아래로, S극은 무조건 위로 밀린다고 생각하면
    N극이 아래로 내려가는 경우만 생각하면 됨
    '''
    for i in range(100):
        # N극 표시용
        flag = False
        for j in range(100):
            # 자석이 있을 경우
            if arr[j][i]:
                # N극일때
                if arr[j][i] == 1:
                    flag = True
                # S극일때
                elif arr[j][i] == 2:
                    # 이미 N극을 만났다면
                    if flag:
                        count += 1
                        flag = False

    print(f'#{test_case} {count}')