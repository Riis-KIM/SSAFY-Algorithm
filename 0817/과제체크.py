T = int(input())

for test_case in range(1, T+1):
    # 수강생 수, 과제 제출한 사람 수
    N, K = map(int, input().split())
    # 제출한 사람
    gwaje = list(map(int, input().split()))

    # 전체 학생
    student = [0] * (N+1)
    # 전체 학생 중 과제를 제출한 사람 표시
    for item in gwaje:
        student[item] = 1

    ans = []
    # 과제 제출 못한 사람 저장
    for i in range(1, N+1):
        if not student[i]:
            ans.append(i)

    print(f'#{test_case}', *ans)