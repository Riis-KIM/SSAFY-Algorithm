
N = int(input())

max_cnt = 0
max_i = 0
# 모든 숫자에 대해서
for i in range(1, N+1):
    # 시작 배열 설정
    arr = [N, i]
    T = 1
    cnt = 1
    tmp = arr[0] - arr[1]
    # 다음 숫자가 음수가 되면 종료
    while tmp >= 0:
        tmp = arr[T-1] - arr[T]
        # 숫자 저장
        arr.append(arr[T-1] - arr[T])
        T += 1
        cnt += 1
    # 음수가 되었을 경우 최대 길이 변경 후 저장, 그때의 다음 숫자 저장
    if max_cnt < cnt:
        max_cnt = cnt
        max_i = i

# 최대 길이일때의 진행과정을 만들기 위함
ans = [N, max_i]
T = 1
tmp = ans[0] - ans[1]
while tmp >=0:
    tmp = ans[T-1] - ans[T]
    if tmp < 0:
        break
    ans.append(tmp)
    T+=1

print(max_cnt, *ans)