T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    # 성적 내림차순으로 정리
    arr.sort(reverse=True)
    # 전체 성적 중 K개만 선택해서 최대 성적을 만드려고 하기 때문에 역순으로 정렬 후 K개 선택
    print(f'#{test_case} {sum(arr[0:K])}')