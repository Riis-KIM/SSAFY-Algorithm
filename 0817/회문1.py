T = 10

for test_case in range(1, T + 1):
    N = int(input())
    arr = [input() for _ in range(8)]

    count = 0

    # 가로 회문 검사
    for i in range(8):
        for t in range(8 - N + 1):
            flag = True
            for j in range(N // 2):  # 문자열의 절반까지
                if arr[i][t + j] != arr[i][t + N - j - 1]:
                    flag = False
                    break
            if flag:
                count += 1

    # 세로 회문 검사
    for i in range(8):
        for t in range(8 - N + 1):
            flag = True
            for j in range(N // 2):  # 문자열의 절반까지
                if arr[t + j][i] != arr[t + N - j - 1][i]:
                    flag = False
                    break
            if flag:
                count += 1

    print(f'#{test_case} {count}')