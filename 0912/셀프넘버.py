def selfnum(n):
    if n > 10000:       # 10000 이상 구할 필요 없음
        return
    ans = n             # 답 저장
    tmp = n             # 나누기 위해 임시변수 저장
    for i in (10000, 1000, 100, 10, 1):         # 셀프 넘버 구함
        ans += tmp // i
        tmp = tmp % i
    arr[ans] = 1          # 해당 배열의 위치에 저장
    selfnum(ans)          # 생성자들을 이용해 생성자의 생성자 확인


arr = [0] * 13000           # 셀프 넘버의 인덱스 오류를 막기 위해 추가적으로 선언
for t in range(1,10001):    # 10000까지 셀프넘버 확인
    if arr[t] == 0:         # 앞에서부터 셀프넘버 확인을 쭉 하는데 여전히 0일 경우만 추가 확인
        selfnum(t)

for i in range(1, 10001):   # 값 출력
    if arr[i] == 0:
        print(i)